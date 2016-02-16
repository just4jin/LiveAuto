#!/usr/bin/env 

from selenium import webdriver
from bs4 import BeautifulSoup as BS

def read_login():
    username = getpass.getpass('\nUsername: ')
	  password = getpass.getpass()
	  return username, password

def web_login(username, password, browser):	
    browser.get("https://aspm.faa.gov/")
	  login = browser.find_element_by_link_text("Login").click()
	  user = browser.find_element_by_id("text1").send_keys(username)
	  passwd = browser.find_element_by_id("password1").send_keys(password)
	  browser.find_element_by_id("submit1").click()
	  return browser
