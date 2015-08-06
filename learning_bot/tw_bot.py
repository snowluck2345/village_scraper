#features to add:
#bubble sort by distances, time stamp attacks, don't attack anything within 1 hour of last attack, later by resource growth rate and attack farming returns
#report scraping
#captcha cracker

import sys
import time
import string
import copy
from optparse import OptionParser
import tribalwars as tw
import csv
import gzip
from splinter import Browser
import os
from PIL import Image
import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
import scipy.io as sio
import re

DATA_DIR_PREFIX = "data/w"
VILLAGES_FILE = "village.txt.gz"

def login():
	browser.driver.maximize_window()
	# Visit URL
	url = "https://www.tribalwars.net"
	browser.visit(url)
	browser.fill('user', '***')
	browser.fill('password', '***')

	time.sleep(random.random())
	# Find and click the 'search' button
	#button = browser.find_by_id('js_login_button')
	# Interact with elements
	#button.click()

	
	browser.execute_script("javascript:document.querySelector('.button_middle').click()")

	time.sleep(random.random())

#	os.system("screencapture screen.jpg")

	time.sleep(random.random())

	browser.find_by_css('.world_button_active').mouse_over()
	browser.find_by_css('.world_button_active').click()


def captcha_check():
	if browser.is_text_present('Bot protection'):
		print('\a')
		print('\a')
		print('\a')
		print('\a')
		print('\a')
		print('\a')
		print('\a')
		print('\a')
		print('\a')
		print('\a')
		captcha = raw_input()
		browser.fill('code', captcha)


def update(lifespan):     

		world = '82'
			   
		# download the data files, if needed, and populate the tribe
		try:
			tw.download_data_files(lifespan, world)
		except tw.WorldError, we:
			sys.exit(we)

def return_villages(world):
	
	data_dir = DATA_DIR_PREFIX + world + "/"

	file = csv.reader(gzip.open(data_dir + VILLAGES_FILE, "rb"))
	k = 0
	for row in file:
		k += 1

	
	village_list = [None] * (k)
	for i in range(k):
		village_list[i] = [None] * 4



	file = csv.reader(gzip.open(data_dir + VILLAGES_FILE, "rb"))

	i = 0
	for row in file:
		village_list[i][0] = int(row[4])
		village_list[i][1] = int(row[2])
		village_list[i][2] = int(row[3])
		village_list[i][3] = int(row[5])
		
		i += 1

	return (k, village_list)

def get_troops():
	axe = browser.find_by_id("units_entry_all_axe")
	if axe:
		temp = re.split('\(', axe.last.value)
		temp = re.split('\)', temp[1])
		num_axe = temp[0]
	else:
		num_axe = 0
	spear = browser.find_by_id("units_entry_all_spear")
	if spear:
		temp = re.split('\(', spear.last.value)
		temp = re.split('\)', temp[1])
		num_spear = temp[0]
	else:
		num_spear = 0
	light = browser.find_by_id("units_entry_all_light")
	if light:
		temp = re.split('\(', light.last.value)
		temp = re.split('\)', temp[1])
		num_light = temp[0]
	else:
		num_light = 0
	print "axe: " + str(num_axe)
	print "spear: " + str(num_spear)
	print "light cavlary: " + str(num_light)	
	return (int(num_spear), int(num_axe), int(num_light))



#main----------------------------------------------------------------------------------------------------------------------------------

update(1)
num_villages, villages = return_villages('82')
my_coordinates = [537, 566]
reduced_villages = []

j = 0
for i in range(num_villages):
	if abs(villages[i][1] - my_coordinates[0]) < 100 and abs(villages[i][2] - my_coordinates[1]) < 100:
#		print villages[i] 
#		print j
		j += 1
		reduced_villages.append(villages[i])

reduced_num_villages = j

print "Close villages: " + str(j)

j = 0

farm_villages = []
for i in range(reduced_num_villages):
	if ((reduced_villages[i][1] - my_coordinates[0])**2 + (reduced_villages[i][2] - my_coordinates[1])**2)**0.5 < 6 and reduced_villages[i][3] < 100:
		farm_villages.append(reduced_villages[i])
		j += 1

num_valid_farms = j

print "Number of farms: " + str(j)
print farm_villages


with Browser() as browser:
	login()
	captcha_check()

	browser.click_link_by_href("/game.php?village=5793&screen=place")
	captcha_check()
	while True:	
		for i in range(1, 50):
			print i
	#		print('\a')
	#		print('\a')
	#		print('\a')

			spear, axe, light_cavalry = get_troops()
			
			while ((spear < 7 or axe < 7) and light_cavalry < 3):
				browser.visit('https://en82.tribalwars.net/game.php?village=5793&screen=overview')
				time.sleep(random.random()*500+500)
				browser.click_link_by_href("/game.php?village=5793&screen=place")
				spear, axe, light_cavalry = get_troops()

		


			time.sleep(random.random()*2.7)

	  #      browser.execute_script("javascript:insertUnit($('#unit_input_light'), 5)")
	  #      browser.execute_script("javascript:insertUnit($('#unit_input_spy'), 1)")

	  		if spear > 6 and axe > 6:
				browser.execute_script("javascript:insertUnit($('#unit_input_axe'), 7)")
				time.sleep(random.random()/2.5)
				browser.execute_script("javascript:insertUnit($('#unit_input_spear'), 7)")
			elif light_cavalry > 2:
				browser.execute_script("javascript:insertUnit($('#unit_input_light'), 3)")
			browser.execute_script("javascript:insertUnit($('#unit_input_spy'), 1)")


			if(int(farm_villages[i][1]) == 530 and int(farm_villages[i][2]) == 557):
				i =+ 1

			time.sleep(random.random()/2.3)
			current_village = str(farm_villages[i][1]) + '|' + str(farm_villages[i][2])
			time.sleep(random.random()/1.7)
			browser.fill('input', current_village)

			button1 = browser.find_by_name('attack')
			button1.click()
			captcha_check()
			time.sleep(random.random()/3)

			button2 = browser.find_by_name('submit')
			print 'hi'
			print button2
			print 'bye'
			button2.click()
			time.sleep(random.random()/2)
			captcha_check()
			time.sleep(random.random())







		
