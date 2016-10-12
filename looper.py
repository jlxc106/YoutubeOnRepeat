#! usr/bin/python
#Written by Jay Lim

from sys import argv
from selenium import webdriver
import time

if len(argv) != 1:
	script, link = argv
else:
	link = raw_input("Enter youtube link: ")

if link.find('youtube.com') == -1:
	print 'Invalid link: get rick rolled'
	link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

chromedriver = '/home/jlxc106/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get(link)

while(1):
	time.sleep(1)
	if driver.execute_script("return document.getElementById('movie_player').getPlayerState()") == 0:
		driver.refresh()
