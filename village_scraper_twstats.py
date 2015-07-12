from bs4 import BeautifulSoup
import re
import scipy.io as sio
import numpy as np

#mat_village_file = sci.loadmat('list.mat')

soup = BeautifulSoup(open("TWStatsTest3.html"))

dschreib_list = soup.find_all(href="index.php?page=village&id=9125")

#print soup.prettify

body = soup.body.find(id="main")
table = body.find(style="width: 100%")


sub_table = table.tr.contents[3]
tbody = sub_table.div.table
contents = tbody.contents

villages = [None] * 200
for i in range(135):
  	villages[i] = [None] * 3

for n in range (3, 273, 2):
	

	print n


	distance = contents[n].contents[1]
	name_and_coordinates = contents[n].contents[5]
	points = contents[n].contents[8]

#	print distance
#	print name_and_coordinates
#	print points
	

	a = n / 2 - 1

	#print "------"

	#print a

	#print distance.string
	#villages[a][0] = float(distance.string)
	#print villages[a][0]
	temp_string = name_and_coordinates.string
	bob = re.split("\(", temp_string)
	bob2 = re.split("\)", bob[-1])
	bob3 = re.split("\|", bob2[0])
#	print bob3[0]
#	print bob3[1]
	villages[a][0] = int(bob3[0])
	villages[a][1] = int(bob3[1])
#	print villages[a][1]
#	print villages[a][2]
	#print villages[a][1]
	villages[a][2] = int(re.sub("[^\d\.]", "", points.string))
	#print villages[a][2]


valid_villages = [None] * 200
for i in range(135):
  	valid_villages[i] = [None] * 3

k = 0
for n in range (0, 135):
	if villages[n][2] < 500 and villages[n][2] > 0 :
		for m in range (0, 3):
			valid_villages[k][m] = villages[n][m]

			#print m
		print "---------"
		print k
		print "---------"
		print valid_villages[k][0]
		print valid_villages[k][1]
		print valid_villages[k][2]
#		print valid_villages[k][3]
		k = k + 1 

#print "-------"
#print k-1
#print valid_villages
#print villages

villages = filter(None, villages)

print '===='

info = np.array(villages)

print info



sio.savemat('clucka.mat', {'test':info})



