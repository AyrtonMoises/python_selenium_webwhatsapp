from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


options = Options()
#PATH_PROFILE = 'C:\\Users\\username\\AppData\\Local\\Google\\Chrome\\User Data\\Profile'
#options.add_argument('--user-data-dir={}'.format(PATH_PROFILE)) #Directory profile save session whatsapp
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(executable_path="D:\\projetos\\selenium_drivers\\chromedriver.exe", options=options)
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))


input('Enter anything after scanning QR code')

try:
    input_search = driver.find_element_by_xpath("//div[@contenteditable='true']")
    input_search.click()
    input_search.send_keys(name)
    time.sleep(2) #wait search

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_xpath("//div[@contenteditable='true'][@spellcheck='true']")
    msg_box.click()

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpath("//span[@data-icon='send']").find_element_by_xpath('..')
        button.click()
        time.sleep(1)

except Exception as e:
    print("Error:", e)
    driver.quit()
