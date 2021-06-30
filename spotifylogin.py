from selenium import webdriver


browser = webdriver.Chrome('/Users/julius/Downloads/chromedriver')

browser.get('https://accounts.spotify.com/de/login?continue=https:%2F%2Fopen.spotify.com%2F')



emailtext = browser.find_element_by_name('username')
emailtext.send_keys('HarmonischSprachloserFrosch@muell.monster')

passwort = browser.find_element_by_name('password')
passwort.send_keys('dasisteintest')

anmeldebutton2 = browser.find_element_by_xpath('//*[@id="login-button"]')
anmeldebutton2.click()





