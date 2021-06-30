from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime




browser = webdriver.Chrome()

browser.get('https://hgo-hs.de/iserv/app/login?target=%2Fiserv%2F')

account = browser.find_element_by_xpath('//*[@id="form-username"]/input')
account.send_keys('jan-paul.albers')

loginpassword = browser.find_element_by_xpath('//*[@id="form-password"]/input')
loginpassword.send_keys('lachenohnelaute')

anmelden = browser.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/form/div[3]/div[1]/button')
anmelden.click()

modulee = browser.find_element_by_xpath('//*[@id="menu-show-more"]')
modulee.click()

videokonf = browser.find_element_by_xpath('//*[@id="menu-wrapper"]/li[20]/a')
videokonf.click()

bio = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div/div/div[1]/div[2]/div/a[1]')
bio.click()
time.sleep(2)
bio.click()

betreten = browser.find_element_by_xpath(
    '//*[@id="content"]/div[2]/div/div/div/div/div[2]/div[1]/div/div/div[1]/a')
betreten.click()

time.sleep(3)
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])

mikro = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[1]')
mikro.click()

time.sleep(13)

ja = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/span/button[1]/span[1]')
ja.click()

time.sleep(3)

mute = browser.find_element_by_class_name('center--ZyfFaC').find_elements_by_tag_name('button')[0]
mute.click()
x = x + 3