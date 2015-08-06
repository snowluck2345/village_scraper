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

    quick_bar = browser.find_by_css("a.quickbar_link")

    browser.execute_script("javascript:$.getScript('https://dl.dropboxusercontent.com/s/kcepyuj6cfrlujb/main.js');void(0);")

  #  quick_bar[5].click()

    time.sleep(10)

    quick_bar[2].click()


