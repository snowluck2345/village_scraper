from splinter import Browser
import time
import os
from PIL import Image
import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
import scipy.io as sio


def login():
    browser.driver.maximize_window()
    # Visit URL
    url = "https://www.tribalwars.net"
    browser.visit(url)
    browser.fill('user', 'dschreib')
    browser.fill('password', 'oblivion')

    time.sleep(random.random())
    # Find and click the 'search' button
    #button = browser.find_by_id('js_login_button')
    # Interact with elements
    #button.click()

    
    browser.execute_script("javascript:document.querySelector('.button_middle').click()")

    time.sleep(random.random())

    os.system("screencapture screen.jpg")

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



village_list_mat = sio.loadmat('daily_farm.mat')
village_list = village_list_mat['test']
print village_list

with Browser() as browser:

    login()

    captcha_check()

    browser.click_link_by_href("/game.php?village=9125&screen=place")

    captcha_check()

    print 
    browser.find_by_id('units_entry_all_axe').value

    for i in range(94, 104):

        print i

        time.sleep(random.random())

        browser.execute_script("javascript:insertUnit($('#unit_input_light'), 5)")
        browser.execute_script("javascript:insertUnit($('#unit_input_spy'), 1)")

        time.sleep(random.random()/3.0)


        current_village = village_list[i][0] + '|' + village_list[i][1]

        time.sleep(random.random()/3.0)

        browser.fill('input', current_village)

        button1 = browser.find_by_name('attack')
        button1.click()

        captcha_check()

        time.sleep(random.random()/3.0)

        button2 = browser.find_by_name('submit')
        button2.click()

        captcha_check()


