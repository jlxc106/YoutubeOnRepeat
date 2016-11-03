#! /usr/bin/python

from sys import argv
from selenium import webdriver
import time

if len(argv) !=1:
	script, link = argv
else:
	link = raw_input("Enter youtube link: ")

chromedriver = '/home/jlxc106/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)

if link.find('youtube.com') == -1:
	driver.get('http://youtube.com')
	time.sleep(1)
	search_box = driver.find_element_by_name('search_query')
	search_box.send_keys(link)
	search_box.submit()
	video_link = driver.find_element_by_partial_link_text(link)
	video_link.click()
else:
	driver.get(link)

while(1):
	time.sleep(1)
	if driver.execute_script("return document.getElementById('movie_player').getPlayerState()") == 0:
		driver.execute_script("return document.getElementById('movie_player').playVideo()")
