#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from datetime import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def loginToAccount(UsrName, Password):
    ## GOES TO INSTAGRAM LOGIN PAGE
    driver.get('https://www.instagram.com/accounts/login/')
    print (driver.title).encode('utf-8')

    ## ENTERS THE USERNAME AND PASSWORD
    user = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
    user.send_keys(UsrName)
    time.sleep(1)
    passwordd = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    passwordd.send_keys(Password)
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    time.sleep(2)
    print (driver.title).encode('utf-8')
    print (driver.current_url)

    ## IF SECURITY CODE IS NEEDED - IT EMAILS AND YOU HAVE TO CHANGE BY YOURSELF AND DEPLOY
    try:

        submit_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Send Security Code')]")))
        submit_button.click()
        time.sleep(10)
        codee = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='securityCode']")))
        codee.send_keys('809532')
        codee.send_keys(u'\ue007')
        time.sleep(20)

        driver.get('https://www.instagram.com/accounts/login/')
        print driver.title.encode('utf-8')

        ## ENTERS THE USERNAME AND PASSWORD
        user = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        user.send_keys(UsrName)
        time.sleep(1)
        passwordd = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        passwordd.send_keys(Password)
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
        time.sleep(2)
        print driver.title.encode('utf-8')
        print (driver.current_url)

    except:
        pass


def enterCelebrityAccountFollowers(url):
    try:
        ## GOES TO THE CELEBRITY ACCOUNT
        driver.get(url)

        ## ENTERS CELEBRITY ACCOUNT FOLLOWERS
        Followers_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
        Followers_button.click()
        print (driver.title).encode('utf-8')
    
    except:
        print 'cant enter celebrity followers'


def getInsideSomeAccount(index):
    try:
        ## ENTERS THE ACCOUNT PROFILE AND WAITS FOR ALL PROFILES TO LOAD - THEN CLICKS ON PROFILE BY INDEX
        WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, '_6e4x5')))  ##ELEMENT NEEDS CHANGE* FINDS ALL LIST ITEMS
        Profile = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@class='_2g7d5 notranslate _o5iw8']")))[
            index]  ## ELEMENT NEEDS CHANGE

        Profile.click()
    
    except:
        pass


def waitUntilTimeReached(FirstTime, SecondTime, TimeDesiredToSleep):
    TimePassed = SecondTime - FirstTime
    SleepingTime = TimeDesiredToSleep - TimePassed

    if SleepingTime < 0:
        return 0

    else:
        return SleepingTime


def GoLatestPostInsideSomeAccount():

    latest_post = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located(
        (By.XPATH, "//*[@class='_mck9w _gvoze _f2mse']")))[0]## NEEDS TO CHANGE !!!!!!!!!

    latest_post.click()



def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)



def LikeActiveAccount():
    AmountOfActiveLikes = 0
    AmountOfFectiveLikes = 0
    index = 0

    enterCelebrityAccountFollowers(celebrityAccountURL)
    getInsideSomeAccount(index)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CLASS_NAME, '_fd86t')))  ##ELEMENT NEEDS CHANGE* WAITS UNTIL THE AMOUNT POSTS ELEMENT IS AVAILABLE

    time.sleep(2)

#     print ("Site At Profile: "), driver.title.encode('utf-8')

    while True:
        try:
            GoLatestPostInsideSomeAccount()
            time.sleep(10)
            print ("Site At Post From: "), driver.title.encode('utf-8')
            break

        except:
            driver.back()
            index += 1
            getInsideSomeAccount(index)
            time.sleep(2)
#             print ("Site At Profile: "), driver.title.encode('utf-8')

    for y in range(0, 24):

        print datetime.today()
        startHour = time.time()

        for x in range(0, 37):

            Heart_Button = driver.find_element_by_xpath("//span[text()='Like']")

            Heart_Button.click()  ## DOES THE LIKE

            now = time.time()

            ## WAITS UNTIL THE LIKE IS DONE
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, ("//span[text()='Unlike']"))))

            enterCelebrityAccountFollowers(celebrityAccountURL)
            index = 0
            while True:

                try:
                    getInsideSomeAccount(index)
                    time.sleep(2)
#                     print ("Site At Profile: "), driver.title.encode('utf-8')

                    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                        (By.CLASS_NAME,'_fd86t')))  ##ELEMENT NEEDS CHANGE* WAITS UNTIL THE AMOUNT POSTS ELEMENT IS AVAILABLE

                    ## CHECKS IF ITS PRIVATE
                    WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located(
                        (By.XPATH, ("//*[@class='_mck9w _gvoze _f2mse']"))))   ##CHECKS IF PRIVATE OR DOESNT HAVE ANY POSTS

                    PostAmount = driver.find_element_by_class_name('_fd86t').text
#                     print ('Number Of Posts: '), PostAmount

                    follow_button1 = driver.find_elements_by_xpath(
                        "//button[contains(.,'Following')]")  ## NO NEED TO CHANGE ELEMENT
                    follow_button2 = driver.find_elements_by_xpath(
                        "//button[contains(.,'Requested')]")  ## NO NEED TO CHANGE ELEMENT


                    ## CHECKS IF ACCOUNT HAS NOT ALREADY BEEN FOLLOWED
                    if follow_button1.__len__() == 0 and follow_button2.__len__() == 0:

                        after = time.time()

                        if int(after) - int(now) > 75:

                            GoLatestPostInsideSomeAccount()

                            WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                                (By.XPATH, ("//span[text()='Like']"))))

                            AmountOfFectiveLikes += 1
                            print ('Fictive Likes: '), AmountOfFectiveLikes
                            break

                        elif 40 <= int(PostAmount) < 200:

                            GoLatestPostInsideSomeAccount()

                            WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                                (By.XPATH, ("//span[text()='Like']"))))

                            date_from_post = driver.find_element_by_tag_name('time')

                            UploadDate = date_from_post.get_attribute('datetime')  ## NO NEED TO CHANGE
                            UploadDate_Correct_Form = UploadDate.split('T')[0]
                            Today = datetime.today().strftime("%Y-%m-%d")
                            Today_Correct_Form = '{}'.format(Today)
                            Days_Difference = days_between(UploadDate_Correct_Form, Today_Correct_Form)

                            if Days_Difference < 21:

                                AmountOfActiveLikes += 1
                                print ('Active Likes: '), AmountOfActiveLikes

                                after = time.time()
                                LoadingTime = waitUntilTimeReached(now, after, 86)
                                time.sleep(LoadingTime)

                                break

                            else:
                                driver.back()


                    index += 1

                    ## AFTER 20 PROFILES, LIST INDEX WILL BE OUT OF RANGE, SO THIS WILL HANDLE
                    if index > 19:
                        index = 0
                        enterCelebrityAccountFollowers(celebrityAccountURL)

                    else:
                        driver.back()

                except Exception as e:  ##IF ITS A PRIVATE ACCOUNT

                    index += 1

                    if index > 19:
                        index = 0
                        enterCelebrityAccountFollowers(celebrityAccountURL)

                    else:
                        driver.back()


        EndHour = time.time()

        LoadinggTimee = waitUntilTimeReached(startHour, EndHour, 3600)

        time.sleep(LoadinggTimee)


    print "AMOUNT OF LIKES DONE FOR TODAY ", (AmountOfActiveLikes + AmountOfFectiveLikes)
    
    
def handleCookies(cookiesList):
    driver.delete_all_cookies()
    
    for cookie in cookiesList:
        try:
            driver.add_cookie(cookie)

        except:
            pass


username = 'alpha__millionaire'
password = '158158123
celebrityAccountURL = 'https://www.instagram.com/arianagrande/'

CounterUntilOneDay = 0

GOOGLE_CHROME_BIN = r"/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = r"/app/.chromedriver/bin/chromedriver"

chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
driver.maximize_window()


loginToAccount(username, password)
# cookies_list = driver.get_cookies()


while True:

    Starting = time.time()
    sta = datetime.today()

    LikeActiveAccount()
#     handleCookies(cookies_list)

    Ending = time.time()
    LoadingDay = waitUntilTimeReached(Starting, Ending, 86520)
    time.sleep(LoadingDay)

    print 'PROGRAM STARTED FOR TODAY', sta
    print 'PROGRAM FINISHED FOR TODAY', datetime.today()

