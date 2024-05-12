from bs4 import BeautifulSoup
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

MULTIPLAYER_FOR_LOADING_SPEED = 2000
LOADING_SPEED = 1
FACEBOOK_GROUP_URL = "https://www.facebook.com/groups/ProgramistaPoczatkujacy"

SCROLL_SCRIPT = "window.scrollTo(0, document.body.scrollHeight);"
cancelCookiesXPATH = "//div[contains(@aria-label, 'Odrzuć opcjonalne pliki cookie')]"
loginQuitXPATH = "//div[contains(@aria-label, 'Zamknij')]"


def cancel_cookies(web_driver):
    cookie_button = web_driver.find_element(By.XPATH, cancelCookiesXPATH)
    cookie_button.click()


def quit_login_popout(webdriver):
    login_quit = webdriver.find_element(By.XPATH, loginQuitXPATH)
    login_quit.click()


def load_page(seconds, webdriver):
    for i in range(0, seconds):
        webdriver.execute_script(SCROLL_SCRIPT)
        time.sleep(LOADING_SPEED)
        print(str(i) + '/' + str(seconds))


def print_comments(parsed_comments):
    number_of_comments = 0
    for line in parsed_comments:
        if line.string and line.string.strip():
            print(line.string.strip())
            number_of_comments += 1
    return number_of_comments


web_driver_instance = webdriver.Chrome()

web_driver_instance.get(FACEBOOK_GROUP_URL)

time.sleep(1)

cancel_cookies(web_driver_instance)

time.sleep(1)

quit_login_popout(web_driver_instance)

time.sleep(1)

load_page(MULTIPLAYER_FOR_LOADING_SPEED, web_driver_instance)

webpage_source = web_driver_instance.page_source

web_driver_instance.close()

parsed_html = BeautifulSoup(webpage_source, 'html.parser')

all_custom_details = parsed_html.find_all('div', {
    'class': 'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs'})

number_of_comments = print_comments(all_custom_details)

print(number_of_comments)
