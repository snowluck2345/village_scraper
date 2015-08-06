import csv
from bs4 import BeautifulSoup
import re
import csv

soup = BeautifulSoup(open("TWStats.html"))

dschreib_list = soup.find_all(href="index.php?page=village&id=9125")

#print soup.prettify

body = soup.body.find(id="main")
table = body.find(style="width: 100%")
sub_table = table.tbody.tr.contents[3]
tbody = sub_table.div.table.tbody
contents = tbody.contents

#contents[2],[4][6]... contain what i want
#1=distance, 5=other village, 8=points
#271 villages --> 2= first, multiples of 2 for villages -> 2 through 272

villages = [None] * 135
for i in range(135):
  	villages[i] = [None] * 3

for n in range (2, 272, 2):
	#print n

	

	distance = contents[n].contents[1]
	name_and_coordinates = contents[n].contents[5]
	points = contents[n].contents[8]

	

	a = n / 2 - 1

	#print "------"

	#print a

	#print distance.string
	villages[a][0] = float(distance.string)
	#print villages[a][0]
	villages[a][1] = name_and_coordinates.string
	#print villages[a][1]
	villages[a][2] = int(re.sub("[^\d\.]", "", points.string))
	#print villages[a][2]


valid_villages = [None] * 135
for i in range(135):
  	valid_villages[i] = [None] * 3

k = 0
for n in range (0, 134):
	if villages[n][2] < 500 and villages[n][0] >= 0 and villages[n][2] > 0  :
		for m in range (0, 3):
			valid_villages[k][m] = villages[n][m]

			#print m
		print "---------"
		print k
		print "---------"
		print valid_villages[k][0]
		print valid_villages[k][1]
		print valid_villages[k][2]
		k = k + 1 

print "-------"
print k-1
#print valid_villages
#print villages





