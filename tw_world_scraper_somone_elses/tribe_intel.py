#!/usr/bin/env python
"""
An example program using the tribalwars module. Basically does it all.

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

import sys
import os.path
import time
import string
import copy
from optparse import OptionParser
import tribalwars as tw


def run(lifespan):     
    while True:
        # get the world number and tribe tag
        #os.system(["clear", "cls"][os.name == "nt"])

        print "\nWelcome to Tribe Intel!\n"
        world = raw_input("World: ").strip(string.whitespace)
        tribe_tag = raw_input("Tribe tag: ").strip(string.whitespace)
        
        if not world or not tribe_tag:
            raw_input("Please enter both a world and tribe tag. Press enter to try again.\n")
            continue
        
        # download the data files, if needed, and populate the tribe
        try:
            tw.download_data_files(lifespan, world)
        except tw.WorldError, we:
            sys.exit(we)

        tribe = tw.populate_tribe(tribe_tag, world)
        
        process_tribe(tribe)

def process_tribe(tribe):
    option = None
    menu = "1. View tribe info\n" + \
           "2. View all members' info\n" + \
           "3. Save all members' info to a CSV file\n" + \
           "4. View a specific member's info\n" + \
           "5. Save a specific member's info to a CSV file\n" + \
           "6. View all tribe villages\n" + \
           "7. Save all tribe villages to a CSV file\n" + \
           "8. Split tribe into platoons\n" + \
           "9. Save tribe platoons to a CSV file\n\n" + \
           "0. Pick a new world and tribe\n\n" + \
           "Please pick an option: "
           
    functions = {"1": print_tribe,
                 "2": print_members,
                 "3": save_members,
                 "4": print_member,
                 "5": save_member,
                 "6": print_villages,
                 "7": save_villages,
                 "8": print_platoons,
                 "9": save_platoons}
           
    while option != "0":
        option = raw_input(menu).strip(string.whitespace)
        
        try:
            functions[option](tribe)
        except KeyError:
            if option != "0" and option != "":
                raw_input("You selected %s, which is not a valid option.\n" % option + \
                          "Press enter to try again.")

def print_tribe(tribe):
    print "\n", tribe, "\n"

def print_members(tribe):
    print
    for member in tribe.members: print member, "\n"

def save_members(tribe):
    tw.save_members(tribe)

def print_member(tribe):
    name = raw_input("Name: ").strip(string.whitespace)
    # TODO catch exception if the name doesn't match anyone
    member = tribe.get_member_by_name(name)
    
    print "\n", member, "\n"
    print "___Villages___"
    
    for village in member.villages: print village, "\n"

def save_member(tribe):
    name = raw_input("Name: ").strip(string.whitespace)
    # TODO catch exception if the name doesn't match anyone
    member = tribe.get_member_by_name(name)

    tw.save_member(member)

def print_villages(tribe):
    for member in tribe.members:
        print "\nPlayer:", member.name
        print "\n__Villages__"

        for village in member.villages:
            print village, "\n\n"

def save_villages(tribe):
    tw.save_villages(tribe)

def print_platoons(tribe):
    platoons = tw.compute_platoons(tribe)

    while len(platoons) >= 3:
        name, continent, quad = platoons[:3]
        print name.ljust(25), continent, quad.ljust(7)
        del platoons[:3] # consume the 3 elements we just printed

    print

def save_platoons(tribe):
    tw.save_platoons(tribe)

if __name__ == "__main__":
    # parse the command line args
    usage = "usage: %prog [options] world_num"
    parser = OptionParser(usage)
    parser.set_defaults(lifespan="1")
    parser.add_option("-l", "--lifespan", dest="lifespan", type="int",
                      help="number of days the world data is considered valid. Defaults to 1 day." + \
                           "A lifespan of 0 days ensures the most current data.")

    options, args = parser.parse_args()
    
    try:
        run(options.lifespan)
    except KeyboardInterrupt:
        # the only reason we're catching the exception here is to surpress the ugly python error
        # that shows when the script is killed with Ctrl-c
        print
