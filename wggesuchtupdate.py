# from seleniumrequests import Firefox
import geckodriver_autoinstaller


geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pickle
import time
from datetime import datetime

def click_if_exists(driver,tag,key,value):
    elems = driver.find_elements_by_xpath("//"+tag+"[@"+key+"]")
    for elem in elems:
        if elem.get_attribute(key)==value:
            # print(elem.get_attribute(key))
            elem.click()
            break


def refresh_wg_gesucht(id,user,pw):
    #headless option for invisible operation
    opts = Options()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)

    driver.get('https://www.wg-gesucht.de/#')


    #cookies
    click_if_exists(driver,"a","class","cmpboxbtn cmpboxbtnyes")

    #click on Login
    click_if_exists(driver,"a","onclick","fireLoginOrRegisterModalRequest('sign_in');ga('send', 'event', 'service_navigation', 'login', '1st_level');")

    #fill in login form
    driver.find_element_by_name("login_email_username").send_keys(user)
    driver.find_element_by_name("login_password").send_keys(pw)

    #press submit
    click_if_exists(driver,"input","id","login_submit")

    #open offer page
    driver.get("https://www.wg-gesucht.de/angebot-bearbeiten.html?action=update_offer&offer_id="+id)

    #click updte
    click_if_exists(driver,"button","id","update_offer_nav")

    # storing the cookies
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    driver.quit()


