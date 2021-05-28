from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import threading
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


driver = None

def main():
    global driver
    options = Options()
    PATH_PROFILE = 'C:\\Users\\T-Gamer\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2'
    options.add_argument('--user-data-dir={}'.format(PATH_PROFILE))
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(executable_path="D:\\projetos\\selenium_drivers\\chromedriver.exe", options=options)
    driver.get('https://web.whatsapp.com/')

    answer = input('Phone connected with success ? (y) -> ')
    if str(answer).strip().lower() == 'y':
        keep_running = True

        while keep_running:
            time.sleep(10) #time to run
            try:
                contacts = ['Teste','Teste', 'Teste']
                for contact in contacts:
                    give_options(contact,['*Title*','Body message'])
                    time.sleep(8)
                
            except:
                keep_running = False

        print('Bot closed')


def give_options(user_name,message,interval=1):
    message_after_interval(interval, user_name.strip(), message)

def message_after_interval(interval, user_name, message):
    threading.Timer(interval, send_message, args=[user_name, message, True]).start()

def open_chat(user_name):
    try:
        print('Search contact..... ' + user_name)
        web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
        web_obj.clear() #clear input

        web_obj.send_keys(user_name)
        time.sleep(2) #wait search

        elem = driver.find_element_by_xpath('//span[@title="{0}"]'.format(user_name))
        elem.click()
        return True
    except:
        print('Contact not found..')
        elem = driver.find_element_by_xpath('//span[@data-icon="x-alt"]')
        elem.click()
        return False


def send_message(user_name, message):
    if open_chat(user_name):
       
        web_obj = driver.find_element_by_xpath("//div[@contenteditable='true'][@spellcheck='true']")
        for row in message:
            web_obj.send_keys(row)
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
            ActionChains(driver).key_up(Keys.ENTER).perform()


if __name__ == '__main__':
    main()