#!/usr/bin/env python
"""
Copyright (c) 2008 Jason Cooper <skawaii at gmail dot com>
under a *slightly* modified MIT License

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, and/or sublicense
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice (including names of original
copyright holders) and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import csv      # read in the data files
import urllib   # URL decode functions
import sys
import os, os.path
import time
import gzip
import copy
from optparse import OptionParser

"""
TODO
- fix populate_all_tribes for tribeless players...and make it faster
- look for uncaught exceptions
- there's always unit testing....
"""

############################# File Formats #################################
# TRIBES_FILE - id, name, tag, members, villages, points, all_points, rank
# PLAYERS_FILE - id, name, ally(tribe id), villages, points, rank
# VILLAGES_FILE - id, name, x, y, tribe(owner id), points, rank
# CONQUERS_FILE - village_id, unix_timestamp, new_owner, old_owner
# PROFILE_FILE - player_id, birthday, gender, location, profile_text (XHTML), picture_filename
############################################################################

TRIBES_FILE = "ally.txt.gz"
PLAYERS_FILE = "tribe.txt.gz"
VILLAGES_FILE = "village.txt.gz"
CONQUERS_FILE = "conquer.txt.gz"
PROFILES_FILE = "profile.txt.gz"
SECS_IN_DAY = 86400
DATA_DIR_PREFIX = "data/w"
CSV_DIR = "CSV/"

class Tribe(object):
    def __init__(self, data):
        """ Tribe([string]) => Tribe
        
            Create a new Tribe instance. Each Tribe has an id, name, tag, num_mumbers, num_villages,
            top_40_points, total_points, and rank.
        """
        self.id = int(data[0])
        self.name = urllib.unquote_plus(data[1])
        self.tag = urllib.unquote_plus(data[2])
        self.num_members = int(data[3])
        self.num_villages = int(data[4])
        self.top_40_points = int(data[5])
        self.total_points = int(data[6])
        self.rank = int(data[7])
        self.members = []
        self.members_ids = []

    def __str__(self):
        return "id: %d\n" % self.id + \
               "name: %s\n" % self.name + \
               "tag: %s\n" % self.tag + \
               "number of members: %d\n" % self.num_members + \
               "number of villages: %d\n" % self.num_villages + \
               "points of top 40: %d\n" % self.top_40_points + \
               "total points: %d\n" % self.total_points + \
               "rank: %d" % self.rank

    def add_member(self, player):
        """ add_player(Player) => void

            Add a single member to this tribe. Once all members of this tribe have
            been added, they are sort by name and their ids are put into a list.
        """
        self.members.append(player)

        if len(self.members) >= self.num_members:
            self.members.sort()
            self.members_ids = [member.id for member in self.members]

    def get_member_by_id(self, id):
        """ get_member_by_id(int) => Player or None
        
            Get a specific member of this tribe using the member's id.
        """
        for member in self.members:
            if member.id == id: return member
            
        return None

    def get_member_by_name(self, name):
        """ get_member_by_name(string) => Player or None

            Get a specific member of this tribe using the member's name.
        """
        for member in self.members:
            if member.name.lower() == name.lower(): return member

        return None


class Player(object):
    def __init__(self, data, world):
        """ Player([string], string) => Player
        
            Create a new Player instance. Each Player has an id, name, tribe_id, num_villages,
            points, rank, and a list of villages.
        """
        self.id = int(data[0])
        self.name = urllib.unquote_plus(data[1]) # url decoding
        self.tribe_id = int(data[2])
        self.num_villages = int(data[3])
        self.points = int(data[4])
        self.rank = int(data[5])
        self.villages = []
        self.area_of_influence = {"continent": "None", "quadrant": "None",
                                  "num_villages": 0, "points": 0}

        # XXX takes too long to parse each player's profile as currently written
        #self.__parse_profile(world)

    def __cmp__(self, other):
        """ Compare based on the players' names """
        return cmp(self.name.lower(), other.name.lower())

    def __str__(self):
        return "id: %d\n" % self.id + \
               "name: %s\n" % self.name + \
               "tribe id: %d\n" % self.tribe_id + \
               "number of villages: %d\n" % self.num_villages + \
               "points: %d\n" % self.points + \
               "rank: %d\n" % self.rank + \
               "area of influence: %s" % str(self.area_of_influence)
               #"birthday: %s\n" % self.birthday + \
               #"gender: %s\n" % self.gender + \
               #"location: %s\n" % self.location + \
               #"profile_text: %s\n" % self.profile_text + \
               #"picture_filename: %s" % self.picture_filename

    def __parse_profile(self, world):
        # PROFILE_FILE - player_id, birthday, gender, location, profile_text (XHTML), picture_filename
        file = csv.reader(gzip.open(DATA_DIR_PREFIX + world + "/" + PROFILES_FILE, "rb"))

        for row in file:
            if int(row[0]) == self.id:
                self.birthday = row[1]
                self.gender = row[2]
                self.location = urllib.unquote_plus(row[3])
                self.profile_text = ""
                self.picture_filename = ""

                # row always has at least 4 elements, but not always 6...dumb
                if len(row) == 5: self.profile_text = urllib.unquote_plus(row[4])
                if len(row) == 6: self.picture_filename = urllib.unquote_plus(row[5])

    def add_village(self, village):
        """ add_village(Village) => void

            Add a single village to a player. Once all villages are added, the are
            sorted by their names and the player's area of influence is determined.
        """
        self.villages.append(village)
        
        if len(self.villages) >= self.num_villages:
            self.villages.sort()
            self.__determine_aoi()

    def get_village(self, x, y):
        """ get_village(int, int) => Village or None

            Get a specific village belonging to this player.
        """
        for village in self.villages:
            if village.x == x and village.y == y: return village

        return None

    def __determine_aoi(self):
        """ __determine_aoi() => void
            
            Determine in which continental quadrant (are of influence - aoi)
            this player is strongest. This is determined based on where
            the most villages are located. If there is a tie, then it's
            based on which quadrant has the most points in it.
        """
        # TODO this is really hacky. not happy with it, but it's ok for now
        continents = {}

        for village in self.villages:
            if village.continent not in continents.keys():
                continents[village.continent] = {}

            if village.quadrant not in continents[village.continent].keys():
                continents[village.continent][village.quadrant] = {"count": 1,
                                                                   "points": village.points}
            else:
                continents[village.continent][village.quadrant]["count"] += 1
                continents[village.continent][village.quadrant]["points"] += village.points

        # time to figure out which continent and quad this player belongs in
        # more lovely hacking
        for continent, quads in continents.items():
            for quad, data in quads.items():
                if data["count"] > self.area_of_influence["num_villages"]:
                    self.area_of_influence["continent"] = continent
                    self.area_of_influence["quadrant"] = quad
                    self.area_of_influence["num_villages"] = data["count"]
                    self.area_of_influence["points"] = data["points"]
                elif data["count"] == self.area_of_influence["num_villages"]:
                    if data["points"] > self.area_of_influence["points"]:
                        self.area_of_influence["continent"] = continent
                        self.area_of_influence["quadrant"] = quad
                        self.area_of_influence["num_villages"] = data["count"]
                        self.area_of_influence["points"] = data["points"]
        

class Village(object):
    def __init__(self, data, world):
        """ Village([string], string) => Village
        
            Create a new Village instance. Each village has an id, name, x, y, player_id (the owenr),
            points, rank, continent, and quadrant.
        """
        self.id = int(data[0])
        self.name = urllib.unquote_plus(data[1]) #url decoding
        self.x = int(data[2])
        self.y = int(data[3])
        self.player_id = int(data[4])
        self.points = int(data[5])
        self.rank = int(data[6])

        # figure out what continent and quadrant the village is in
        self.continent = self.y / 100 * 10 + self.x / 100
        self.quadrant = self.__compute_quadrant()

    def __cmp__(self, other):
        """ Compare based on the villages' names """
        return cmp(self.name.lower(), other.name.lower())

    def __str__(self):
        return "id: %d\n" % self.id + \
               "name: %s\n" % self.name + \
               "x: %d\n" % self.x + \
               "y: %d\n" % self.y + \
               "continent: K%d\n" % self.continent + \
               "quadrant: %s\n" % self.quadrant + \
               "player_id: %d\n" % self.player_id + \
               "points: %d\n" % self.points + \
               "rank: %d" % self.rank

    def __compute_quadrant(self):
        """ __compute_quadrant() => string
        
            Based on the villages x and y coordinates, figure out which quadrant (NE, NW, SE, SW)
            this village should be in.
        """
        # only need the tens and ones digits
        x_part = self.x % 100
        y_part = self.y % 100

        quad = None

        if x_part <= 49:
            if y_part <= 49: quad = "NW"
            else: quad = "SW"
        else:
            if y_part <= 49: quad = "NE"
            else: quad = "SE"

        return quad


class WorldError(Exception):
    def __init__(self, world, message):
        """ WorldError(int, string) => void
            
            Exception for any error related to a TW world.
        """
        self.world = world
        self.message = message

    def __str__(self):
        return "\nWorldError: World " + self.world + "- " + self.message


def download_data_files(lifespan, world):
    data_dir = DATA_DIR_PREFIX + world + "/"

    # check if the data directory exists
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
        __download_data_files(data_dir, world)

    # make sure all the data files are there
    if not os.path.isfile(data_dir + TRIBES_FILE) or not os.path.isfile(data_dir + PLAYERS_FILE) \
            or not os.path.isfile(data_dir + VILLAGES_FILE) or not os.path.isfile(data_dir + CONQUERS_FILE) \
            or not os.path.isfile(data_dir + PROFILES_FILE):
        __download_data_files(data_dir, world)

    # check the time on the tribes file to see if we should re-download
    ctime = os.stat(data_dir + TRIBES_FILE).st_ctime
    
    if time.time() - ctime >= lifespan * SECS_IN_DAY: __download_data_files(data_dir, world)

def __download_data_files(data_dir, world):
    """ Download the 5 data files from the Tribal Wars server"""
    base_url = "http://en" + world + ".tribalwars.net/map/"

    try:
        sys.stdout.write("\nDownloading ally.txt.gz...")
        sys.stdout.flush()
        urllib.urlretrieve(base_url + TRIBES_FILE, data_dir + TRIBES_FILE)
        urllib.urlcleanup()
        sys.stdout.write("Done\n")

        sys.stdout.write("Downloading tribe.txt.gz...")
        sys.stdout.flush()
        urllib.urlretrieve(base_url + PLAYERS_FILE, data_dir + PLAYERS_FILE)
        urllib.urlcleanup()
        sys.stdout.write("Done\n")

        sys.stdout.write("Downloading village.txt.gz...")
        sys.stdout.flush()
        urllib.urlretrieve(base_url + VILLAGES_FILE, data_dir + VILLAGES_FILE)
        urllib.urlcleanup() # clear the cache
        sys.stdout.write("Done\n")
    
        sys.stdout.write("Downloading conquer.txt.gz...")
        sys.stdout.flush()
        urllib.urlretrieve(base_url + CONQUERS_FILE, data_dir + CONQUERS_FILE)
        urllib.urlcleanup()
        sys.stdout.write("Done\n")

        sys.stdout.write("Downloading profile.txt.gz...")
        sys.stdout.flush()
        urllib.urlretrieve(base_url + PROFILES_FILE, data_dir + PROFILES_FILE)
        urllib.urlcleanup()
        sys.stdout.write("Done\n")
    except IOError:
        raise WorldError(world, "Invalid world number")

def populate_all_tribes(world):
    """ populate_all_tribes(string) => dict
    
        Get a dictionary of all the tribes in a single game world. The dictionary
        keys are the tribe tags. 
        NOTE that right now this is really slow (takes about 30 mins). Don't
             recommend using this function in its current form.
    """
    data_dir = DATA_DIR_PREFIX + world + "/"
    tribes = {}
    tribe_ids = {}
    
    # get all the tribes
    file = csv.reader(gzip.open(data_dir + TRIBES_FILE, "rb"))
    
    for row in file:
        tribes[row[2]] = Tribe(row)
        tribe_ids[int(row[0])] = row[2]
    
    # add all the players to their tribe
    file = csv.reader(gzip.open(data_dir + PLAYERS_FILE, "rb"))
    
    for row in file:
        if int(row[2]) == 0: continue
        tribes[tribe_ids[int(row[2])]].add_member(Player(row, world))
    
    # add all the villages to their owners
    file = csv.reader(gzip.open(data_dir + VILLAGES_FILE, "rb"))
    
    for row in file:
        for tribe in tribes.values():
            owner_id = int(row[4])
            
            if owner_id in tribe.members_ids:
                tribe.get_member_by_id(owner_id).add_village(Village(row, world))
                break

    return tribes

def populate_tribe(tribe_tag, world):
    """ populate_tribe(string, string) => Tribe or None

        Get a fully-populated tribe (meaning you have all tribe info, player
        info, and village info). The tribe is matched by the supplied tribe
        tag.
    """
    sys.stdout.write("\nPopulating tribe...")
    sys.stdout.flush()
    
    data_dir = DATA_DIR_PREFIX + world + "/"
    tribe = None
    
    file = csv.reader(gzip.open(data_dir + TRIBES_FILE, "rb"))

    for row in file:
        if urllib.unquote_plus(row[2]).lower() == tribe_tag.lower():
            tribe = Tribe(row)
            break

    #TODO throw exception if tribe is None (invalid tribe tag)

    # add players to the tribe and get a list of their ids
    file = csv.reader(gzip.open(data_dir + PLAYERS_FILE, "rb"))
    
    for row in file:
        if int(row[2]) == tribe.id:
            tribe.add_member(Player(row, world))

    # get all villages added to the correct Player
    file = csv.reader(gzip.open(data_dir + VILLAGES_FILE, "rb"))

    for row in file:
        owner_id = int(row[4])
        
        if owner_id in tribe.members_ids:
            [member.add_village(Village(row, world)) for member in tribe.members if member.id == owner_id]

    print "Done\n"
    return tribe

def compare_player_regions(player1, player2):
    """ compare_player_regions(Player, Player) => int
    
        Compares tw players based on their area of influence and name.
        The exact order is continent, quad (NW, NE, SW, SE), and name.
        Returns -1, 0. or 1 depending on whether player1 is considered
        smaller, equal, or greater than player2.
    """
    continent_cmp = cmp(player1.area_of_influence["continent"], player2.area_of_influence["continent"])
    
    if not continent_cmp:
        quad_cmp = cmp(player1.area_of_influence["quadrant"], player2.area_of_influence["quadrant"])
        
        if not quad_cmp: return cmp(player1.name.lower(), player2.name.lower())
        else: return quad_cmp
    else:
        return continent_cmp

def compute_platoons(tribe):
    """ compute_platoons(Tribe) => [string]

        Computes the platoons for a given tribe and returns the info
        as a list of strings.
    """
    # sort the tribe members by region (w/o changing original list)
    members = copy.deepcopy(tribe.members)
    members.sort(compare_player_regions)

    # put the platoon info into a list of strings
    platoons = []

    for member in members:
        platoons.append(member.name)
        platoons.append("K" + str(member.area_of_influence["continent"]))
        platoons.append(member.area_of_influence["quadrant"])

    return platoons

def save_platoons(tribe, filepath=""):
    """ save_platoons(Tribe, string) => void

        Compute and save tribe platoons to a CSV file (Excel dialect).
        NOTE: the filepath argument is presently ignored
    """
    # create the CSV directory (if needed) and build the absolute filepath
    if not os.path.isdir(CSV_DIR): os.makedirs(CSV_DIR)
    filepath = os.path.abspath(CSV_DIR + tribe.tag + "_platoons.csv")
    
    writer = csv.writer(open(filepath, "wb"))
    writer.writerow(["Name", "Continent", "Quadrant"]) # CSV header
    
    platoons = compute_platoons(tribe)

    while len(platoons) >= 3:
        writer.writerow(platoons[:3])
        del platoons[:3]

    print filepath, "successfully saved.\n"

def save_members(tribe, filepath=""):
    """ save_member(Tribe, string) => void

        Save the tribe's member info to a CSV file (Excel dialect).
        NOTE: the filepath argument is presently ignored
    """
    # create the CSV directory (if needed) and build the absolute filepath
    if not os.path.isdir(CSV_DIR): os.makedirs(CSV_DIR)
    filepath = os.path.abspath(CSV_DIR + tribe.tag + "_members.csv")
    
    writer = csv.writer(open(filepath, "wb"))
    # write the header row
    writer.writerow(["Name", "Number of Villages", "Points", "Rank", "AOI Continent",\
                     "AOI Quadrant", "AOI Number of Villages", "AOI Points"])

    for member in tribe.members:
        writer.writerow([member.name, member.num_villages, member.points, member.rank,\
                         "K" + str(member.area_of_influence["continent"]), member.area_of_influence["quadrant"],\
                         member.area_of_influence["num_villages"], member.area_of_influence["points"]])
    
    print filepath, "successfully saved.\n"

def save_villages(tribe, filepath=""):
    """ save_villages(Tribe, string) => void

        Save the tribe's villages info to a CSV file (Excel dialect).
        NOTE: the filepath argument is presently ignored
    """
    # create the CSV directory (if needed) and build the absolute filepath
    if not os.path.isdir(CSV_DIR): os.makedirs(CSV_DIR)
    filepath = os.path.abspath(CSV_DIR + tribe.tag + "_villages.csv")

    writer = csv.writer(open(filepath, "wb"))
    # write the header row
    writer.writerow(["Player", "Village Name", "X", "Y", "Continent", "Quadrant", "Points", "Rank"])

    for member in tribe.members:
        writer.writerow([member.name])

        for village in member.villages:
            writer.writerow(["", village.name, village.x, village.y, village.continent,
                             village.quadrant, village.points, village.rank])

    print filepath, "successfully saved.\n"

def save_member(member, filepath=""):
    """ save_member(Player, string) => void

        Save the member's info to a CSV file (Excel dialect).
        NOTE: the filepath argument is presently ignored
    """
    # create the CSV directory (if needed) and build the absolute filepath
    if not os.path.isdir(CSV_DIR): os.makedirs(CSV_DIR)
    filepath = os.path.abspath(CSV_DIR + member.name + ".csv")
    
    writer = csv.writer(open(filepath, "wb"))
    # write the player info header row and the info
    writer.writerow(["Name", "Number of Villages", "Points", "Rank", "AOI Continent",\
                     "AOI Quadrant", "AOI Number of Villages", "AOI Points"])

    writer.writerow([member.name, member.num_villages, member.points, member.rank,\
                     "K" + str(member.area_of_influence["continent"]), member.area_of_influence["quadrant"],\
                     member.area_of_influence["num_villages"], member.area_of_influence["points"]])

    writer.writerow([]) # write a blank line

    # write the player's village header and info
    writer.writerow(["Village Name", "X", "Y", "Continent", "Quadrant", "Points", "Rank"])

    for village in member.villages:
        writer.writerow([village.name, village.x, village.y, village.continent, village.quadrant,\
                         village.points, village.rank])
    
    print filepath, "successfully saved.\n"


def return_villages(world):
    
    
    data_dir = DATA_DIR_PREFIX + world + "/"
    
    #file = csv.reader(gzip.open(data_dir + TRIBES_FILE, "rb"))

    #for row in file:
    #    if urllib.unquote_plus(row[2]).lower() == tribe_tag.lower():
    #        tribe = Tribe(row)
    #        break

    #TODO throw exception if tribe is None (invalid tribe tag)

    # add players to the tribe and get a list of their ids
    #file = csv.reader(gzip.open(data_dir + PLAYERS_FILE, "rb"))
    
    #for row in file:
    #    if int(row[2]) == tribe.id:
    #        tribe.add_member(Player(row, world))

    # get all villages added to the correct Player
    file = csv.reader(gzip.open(data_dir + VILLAGES_FILE, "rb"))

    for row in file:
        owner_id = int(row[4])
        
        if owner_id in tribe.members_ids:
            [member.add_village(Village(row, world)) for member in tribe.members if member.id == owner_id]

    print "Done\n"
    return tribe


if __name__ == "__main__":
    print "Nothing to see here! Run tribe_intel.py instead."

    """
    # parse the command line args
    usage = "usage: %prog [options] world_num"
    parser = OptionParser(usage)
    parser.set_defaults(lifespan="1")
    parser.add_option("-l", "--lifespan", dest="lifespan", type="int",
                      help="number of days the world data is considered valid. Defaults to 1 day." + \
                           "A lifespan of 0 days ensures the most current data.")

    options, args = parser.parse_args()

    # make sure they entered a world and tribe tag
    if len(args) != 2:
        parser.error("\tPlease enter a world number and a tribe tag.\n" + \
                     "\t\t\tExample: tribalwars.py 7 ABC\n" + \
                     "\t\t\tType 'python tribalwars.py -h' for more help.")

    world = args[0]
    tribe_tag = args[1]

    # download data files, if needed
    download_data_files(options.lifespan, world)

    # parse all the info for the tribe, its players, and their villages
    tribe = populate_tribe(tribe_tag, world)

    # do whatever you want with the tribe now
    print tribe
    """
