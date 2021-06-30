#Einbindung der Libarys
import time
from selenium import webdriver
import datetime
x = 2

#Zeitstart und Formatierung der aktuellen Zeit
timenow = datetime.datetime.now().time()
timenow2 = timenow.strftime(format="%H:%M:%S")



#Inputs
timo = input('Uhrzeit mit Doppelpunkten und Sekunden angeben z.B.' + timenow2 + ' Hier einfügen: ')
farbe = input('Herstellerfarben: ')
name = input('Schuhname: ')
große = input('Größe: ')
ppassword = input('Paypal Passwort bitte angeben: ')
ppemail = input('Paypal Email bitte angeben: ')

#Zeitformatierung des Inputs
time2 = timo.replace(':', '')
time3 = int(time2)

#URL Generator
farbe2 = farbe.replace(' ', '-')
farbe3 = farbe2.replace ('/-', '')
URL = 'https://www.asphaltgold.com/de/product/' + name + '-' + farbe3 + '/'
URL2 = URL.replace(' ', '-')
URL3 = URL2.lower()



#Durchgängige Überprüfung der Zeit
while x != 5:
    the_time = datetime.datetime.now().time()

    the_time_2 = the_time.strftime(format="%H:%M:%S")
    the_time_3 = the_time_2.replace(':', '')                    #Zeitformatierung der Abgerufenen Zeit
    the_time_4 = int(the_time_3)


    if the_time_4 < time3:                                      #Wenn Zeit noch nicht erreicht ist
        print('Noch nicht')


    else:                                                       #Wenn Zeit überschritten wurde
        print('NOW')

        #Browser Aufsetzen
        browser = webdriver.Chrome('/Users/julius/Downloads/chromedriver')
        browser.get(URL3)

        #Cookies akzeptieren
        time.sleep(2)
        cookies = browser.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]')
        cookies.click()

        #Größe auswählen
        größe = browser.find_element_by_xpath('/html/body/app-root/main/div/app-product-detail/div/div[1]/div[2]/div/lib-size-selection/div/ul/li[1]/button')
        größe.click()





        #Checkout beginnt
        wagen = browser.find_element_by_xpath('/html/body/app-root/main/div/app-product-detail/div/div[1]/div[2]/div/section[4]/lib-button/button')
        wagen.click()

        time.sleep(2)

        weiter = browser.find_element_by_xpath('//*[@id="mat-dialog-0"]/lib-cart-layer/mat-dialog-actions/section/lib-button/button')
        weiter.click()

        time.sleep(2)

        #VersandInfos
        email = browser.find_element_by_xpath('//*[@id="mat-input-10"]')
        email.send_keys('GeliebtZuverlaessigerBasilisk@wellick.ru')
        vorname = browser.find_element_by_xpath('//*[@id="mat-input-1"]')
        vorname.send_keys('Maximilian')
        nachname = browser.find_element_by_xpath('//*[@id="mat-input-2"]')
        nachname.send_keys('Metzger')
        straße = browser.find_element_by_xpath('//*[@id="mat-input-3"]')
        straße.send_keys('Schafgarbenweg 48')
        post = browser.find_element_by_xpath('//*[@id="mat-input-6"]')
        post.send_keys('26135')
        stadt = browser.find_element_by_xpath('//*[@id="mat-input-7"]')
        stadt.send_keys('Oldenburg')
        tel = browser.find_element_by_xpath('//*[@id="mat-input-8"]')
        tel.send_keys('01758010045')
        time.sleep(2)
        region = browser.find_element_by_xpath('//*[@id="mat-select-2"]/div')
        region.click()

        time.sleep(3)

        nieder = browser.find_element_by_xpath('//*[@id="mat-option-86"]/span')
        nieder.click()

        #Zahlung

        time.sleep(7)

        paypal = browser.find_element_by_xpath('//*[@id="mat-radio-8"]')
        paypal.click()
        time.sleep(3)
        anmeldung = browser.find_element_by_xpath('/html/body/app-root/main/div/app-checkout/div/form/section[2]/app-checkout-snippet-payment-methods/div/mat-radio-group/div[1]/div[2]/lib-base-dynamic-form/div/lib-paypal-button/lib-button/button')
        anmeldung.click()

        time.sleep(5)

        print(browser.window_handles)
        browser.switch_to_window(browser.window_handles[1])             #Das Fenster wird gewechselt um sich bei Paypal anzumelden
        time.sleep(3)
        cookies2 = browser.find_element_by_xpath('//*[@id="acceptAllButton"]')
        cookies2.click()

        pemail = browser.find_element_by_xpath('//*[@id="email"]')
        pemail.send_keys(ppemail)
                                                  #Angegebene Email wird eingefügt

        cont = browser.find_element_by_xpath('//*[@id="btnNext"]')
        cont.click()

        time.sleep(2)

        passwort = browser.find_element_by_xpath('//*[@id="password"]')
        passwort.send_keys(ppassword)                                          #Angegebenes Passwort wird eingefügt

        login = browser.find_element_by_xpath('//*[@id="btnLogin"]')
        login.click()
        time.sleep(3)
        order = browser.find_element_by_xpath('//*[@id="payment-submit-btn"]')
        order.click()

        x = x + 3                                                       #Dient nur dazu das die While Schleife sich nicht wiederholt

print('Succesfull')