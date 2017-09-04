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
        codee.send_keys('647928')
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
    ## GOES TO THE CELEBRITY ACCOUNT
    driver.get(url)

    ## ENTERS CELEBRITY ACCOUNT FOLLOWERS
    Followers_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
    Followers_button.click()
#     print (driver.title).encode('utf-8')


def getInsideSomeAccount(index):
    ## ENTERS THE ACCOUNT PROFILE AND WAITS FOR ALL PROFILES TO LOAD - THEN CLICKS ON PROFILE BY INDEX
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, '_6e4x5')))  ##ELEMENT NEEDS CHANGE* FINDS ALL LIST ITEMS
    Profile = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@class='_2g7d5 notranslate _o5iw8']")))[
        index]  ## ELEMENT NEEDS CHANGE

    Profile.click()


def waitUntilTimeReached(FirstTime, SecondTime, TimeDesiredToSleep):
    TimePassed = SecondTime - FirstTime
    SleepingTime = TimeDesiredToSleep - TimePassed

    if SleepingTime < 0:
        return 0

    else:
        return SleepingTime


def GoLatestPostInsideSomeAccount():

    latest_postUrl = WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located(
        (By.XPATH, "//*[@class='_mck9w _gvoze _f2mse']")))[0].find_element_by_tag_name('a').get_attribute('href')  ## NEEDS TO CHANGE !!!!!!!!!

    driver.get(latest_postUrl)


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)



def LikeActiveAccount():
    AmountOfActiveLikes = 0
    AmountOfFectiveLikes = 0
    index = 0
    now = time.time()

    enterCelebrityAccountFollowers(celebrityAccountURL)
    getInsideSomeAccount(index)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CLASS_NAME, '_fd86t')))  ##ELEMENT NEEDS CHANGE* WAITS UNTIL THE AMOUNT POSTS ELEMENT IS AVAILABLE

    time.sleep(2)

#     print ("Site At Profile: "), driver.title.encode('utf-8')

    while True:
        try:
            GoLatestPostInsideSomeAccount()
            time.sleep(2)
#             print ("Site At Post From: "), driver.title.encode('utf-8')
            break

        except:
            enterCelebrityAccountFollowers(celebrityAccountURL)
            index = 0
            getInsideSomeAccount(index)
            time.sleep(2)
#             print ("Site At Profile: "), driver.title.encode('utf-8')

    for y in range(0, 24):
        
        print datetime.today()
        StartHour = time.time()

        for x in range(0, 40):

            Heart_Button = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, ("//span[text()='Like']"))))
            
            after = time.time()
            
            LoadingTime = waitUntilTimeReached(now, after, 88)
            
            time.sleep(LoadingTime)

            Heart_Button.click()  ## DOES THE LIKE

            now = time.time()
            
            time.sleep(2)
            driver.refresh()

            ## WAITS UNTIL THE LIKE IS DONE
            WebDriverWait(driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, ("//span[text()='Unlike']"))))

            AmountOfFectiveLikes += 1

            enterCelebrityAccountFollowers(celebrityAccountURL)
            index = 0
            while True:

                try:
                    getInsideSomeAccount(index)
                    time.sleep(2)
#                     print ("Site At Profile: "), driver.title.encode('utf-8')

                    ## CHECKS IF ITS PRIVATE

                    WebDriverWait(driver, 2).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//*[@class='_mck9w _gvoze _f2mse']")))[0] \
                        .find_element_by_tag_name('a').get_attribute('href')  ## NEEDS TO CHANGE !!!!!

                    PostAmount = driver.find_element_by_class_name('_fd86t').text
#                     print ('Number Of Posts: '), PostAmount

                    follow_button1 = driver.find_elements_by_xpath(
                        "//button[contains(.,'Following')]")  ## NO NEED TO CHANGE ELEMENT
                    follow_button2 = driver.find_elements_by_xpath(
                        "//button[contains(.,'Requested')]")  ## NO NEED TO CHANGE ELEMENT


                    ## CHECKS IF ACCOUNT HAS NOT ALREADY BEEN FOLLOWED
                    if follow_button1.__len__() == 0 and follow_button2.__len__() == 0:

                        after = time.time()

                        if int(after) - int(now) > 82:
                            GoLatestPostInsideSomeAccount()
                            AmountOfFectiveLikes += 1
#                             print ('Fictive Likes: '), AmountOfFectiveLikes
                            break

                        elif 40 <= int(PostAmount) < 200:
                            GoLatestPostInsideSomeAccount()

                            ## THIS CALCULATES THE DAYS BETWEEN TODAY AND THE UPLOAD DATE (AND PUTS IT IN CORRECT FORM)
                            date_from_post = WebDriverWait(driver, 2)\
                                .until(EC.presence_of_element_located((By.TAG_NAME, 'time'))) ## NO NEED TO CHANGE
                            UploadDate = date_from_post.get_attribute('datetime')  ## NO NEED TO CHANGE
                            UploadDate_Correct_Form = UploadDate.split('T')[0]
                            Today = datetime.today().strftime("%Y-%m-%d")
                            Today_Correct_Form = '{}'.format(Today)
                            Days_Difference = days_between(UploadDate_Correct_Form, Today_Correct_Form)

                            if Days_Difference < 21:
#                                 print ('Active Likes: '), AmountOfActiveLikes
                                AmountOfActiveLikes += 1
                                break

                            else:
                                enterCelebrityAccountFollowers(celebrityAccountURL)
                                index = 0

                        else:
                            ## IF, ONE OF THE IF'S STATEMENTS ARE FALSE, DRIVER GOES BACK TO LIST TO TRY NEXT ACCOUNT
                            index += 1

                            ## AFTER 20 PROFILES, LIST INDEX WILL BE OUT OF RANGE, SO THIS WILL HANDLE
                            if index > 19:
                                index = 0
                                enterCelebrityAccountFollowers(celebrityAccountURL)

                            else:
                                driver.back()

                except:
                    driver.back()
                    index += 1
                    getInsideSomeAccount(index)
        
        EndHour = time.time()
        LoadingggTime = waitUntilTimeReached(StartHour, EndHour, 3600)
        time.sleep(LoadingggTime)
        
        print ("LIKED :"), (AmountOfFectiveLikes + AmountOfActiveLikes), ("ACCOUNTS THIS HOUR")
        
    sumLikes = AmountOfActiveLikes + AmountOfFectiveLikes
    print ("NUMBER OF LIKES DONE FOR TODAY: "), sumLikes

username = 'puberty_goals.09'
password = '158123RA'
celebrityAccountURL = 'https://www.instagram.com/garethbale11/'

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

while True:
#     noww = time.time()
    LikeActiveAccount()
    
#     afterr = time.time()
#     LoadinggTime = waitUntilTimeReached(noww, afterr, 86520)
#     time.sleep(LoadinggTime)

  
