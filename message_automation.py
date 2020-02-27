
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import docx
import os

def web_automation(text_message, phone_number):
    # Define the URL's we will open and a few other variables 
    main_url = 'https://messages.google.com/web/conversations' # URL A
    # tab_url = 'https://www.google.com' # URL B
    chromedriver = 'chromedriver'
    # Open main window with URL A
    browser= webdriver.Chrome(chromedriver)
    browser.get(main_url)
    time.sleep(20)
    wait = WebDriverWait(browser, 50)

    start_chat_btn = browser.find_element_by_xpath('/html/body/mw-app/div/main/mw-main-container/div[1]/mw-main-nav/div/mw-fab-link/a')
    start_chat_btn.click()

    time.sleep(1)
    text_input_box = browser.find_element_by_xpath('//*[@id="mat-chip-list-0"]/div/input')
    text_input_box.send_keys('01770755333')
    text_input_box.send_keys(Keys.ENTER)

    time.sleep(1)
    message_field = browser.find_element_by_xpath('/html/body/mw-app/div/main/mw-main-container/div[1]/mw-conversation-container/div/div/mws-message-compose/div/div[2]/div/mws-autosize-textarea/textarea')
    message_field.send_keys('Hello dude.')
    message_field.send_keys(Keys.ENTER)


def read_text_message():
    text = docx.Document(os.path.abspath('text'))
    print(text)


read_text_message()