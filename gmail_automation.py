from selenium import webdriver
import time
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

browser.get('https://accounts.google.com/ServiceLogin/signinchooser?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&osid=1&service=mail&ss=1&ltmpl=default&rm=false&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

email = browser.find_element_by_name('identifier')

email.send_keys(em)

next = browser.find_element_by_id('identifierNext')
 
next.click()

time.sleep(5)

pwd = browser.find_element_by_css_selector('div.I0VJ4d > div.Xb9hP > input')

pwd.send_keys(pawd)

sub = browser.find_element_by_id('passwordNext')

sub.click()