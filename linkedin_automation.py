from selenium import webdriver
import pyautogui as pg ,time
from getpass import getpass

# option 1: if you want to don't want to write email and password every time you login,
# kindly store your detail below:

em = ''  # write email address here between comma.

pawd = ''  # write password here between comma.

# option 2: if you don't want to store email and password, then uncomment below two line number 15 & 17
# and comment above two lines i.e. line number 8 & 10

#em = input('enter email : ')

#pawd = getpass('enter password:')



browser = webdriver.Chrome('C:\\Users\\admin\\Desktop\\chromedriver.exe')

browser.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')

email = browser.find_element_by_id('username')

email.send_keys(em) 

pwd = browser.find_element_by_id('password')

pwd.send_keys(pawd) 

submit = browser.find_element_by_css_selector('.from__button--floating')

submit.click()