from bs4 import BeautifulSoup
import re
import scipy.io as sio
import numpy as np

#mat_village_file = sci.loadmat('list.mat')

soup = BeautifulSoup(open("smaller.html"))

data = soup.find_all(class_= 'quickedit-label')

bob =  re.split("\(", data[0].string)
bob2 = re.split("\)", bob[-1])
bob3 = re.split("\|", bob2[0])

villages = [None] * 200
for i in range(200):
  	villages[i] = [None] * 2

for n in range(200):

	bob =  re.split("\(", data[n].string)
	bob2 = re.split("\)", bob[-1])
	bob3 = re.split("\|", bob2[0])

	villages[n][0] = bob3[0]
	villages[n][1] = bob3[1]

info = np.array(villages)
#print info
sio.savemat('daily_farm.mat', {'test':info})

village_list_mat = sio.loadmat('daily_farm.mat')
village_list = village_list_mat['test']


print village_list


