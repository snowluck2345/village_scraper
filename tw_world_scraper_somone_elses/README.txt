I. INTRODUCTION

tribalwars is a Python library providing some handy functions and classes.
It is not, in itself, a program/application that will do things out of the
box. The intent is that this library will help automate various tasks
(download files, parse the files, etc) so that you can do more interesting things.

II. DOWNLOADING TRIBAL WARS DATA FILES

The tribalwars library has methods to automatically downloaded the needed data
files from Tribal Wars. These data files are saved in the a subdirectory of
where tribalwars.py is saved.

For example, if you downloaded tribalwars-xxx.zip to your desktop on Windows and
unzipped it to a directory named tribalwars, then the data files would downloaded
to <desktop>\tribalwars\data\w<num>.

By default, the three data files are only downloaded if they are older than one day.
If you want to keep the files around for longer than one day, then set the lifespan
option when running the script.

For example, if you wanted to keep the data files for three days, then run the script
as follows:

python tribal_intel.py -l3 OR python tribal_intel.py --lifespan=3

III. EXAMPLE USAGE

For examples on using the tribalwars library, see the accompanying tribal_intel.py
script or simply leave a question on the Questions page.

IV. RUNNING THE TRIBAL_INTEL SCRIPT

In order to execute these scripts, you need to have Python installed (at least
version 2.3). You can download Python for free at http://www.python.org/download.

In Mac OS X, you can run the script by opening up Terminal (Applications > Utility
or just search for it in Spotlight). In Terminal, go to the directory where you
downloaded tribalwars to and unzip the archive (if you already haven't). Then type:

python tribal_intel.py

In Linux, open up a terminal and type the same command as above:

python tribal_intel.py

In Windows, you can normally simply double-click on the tribal_intel.py and it will
run. You can also open up the command line (Start > Run > cmd), go to the location
of tribal_intel.py, and -- you guessed it -- type:

python tribal_intel.py

When you want to quit tribal_intel, just press Ctrl-c.
