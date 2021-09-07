from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#################################################################################################
#                                                                                               #
#   name:   Jenny Kim                                                                           #
#   email:  yjkim@usc.edu                                                                       #
#                                                                                               #
#   How To:                                                                                     #
#   1. Download chromedriver: https://chromedriver.chromium.org/downloads                       #
#   2. Unzip chromedriver and put into source folder with this .py file                         #
#   3. Install selenium                                                                         #
#   3. Fill in the to-do's in the job() function                                                #
#   4. Create a folder to hold image                                                            #
#   5. To automate using cron, schedule like this (these steps schedules for 6 am)              #
#       In terminal:                                                                            #
#       export VISUAL=nano; crontab -e                                                          #
#        0 6 * * * PYTHONPATH=<path_to_python> python <path_to_main.py>                         #
#        ^o, enter, ^x                                                                          #
#                                                                                               #
#################################################################################################


def job():
    # TODO: specify path to chromedriver in same folder
    driver = webdriver.Chrome(executable_path='')

    # get trojan check url
    driver.get("https://trojancheck.usc.edu/login")

    # log in information
    login_button = \
        driver.find_elements_by_xpath('/html/body/app-root/app-login/main/section/div/div[1]/div/div[1]/button')[
            0]
    login_button.click()
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
    username = driver.find_element_by_id('username')
    username.clear()

    # TODO: set username
    username.send_keys("tommy trojan")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))

    password = driver.find_element_by_id('password')
    password.clear()
    # my_password = input("Enter your password")
    # TODO: set password below or log in each time (uncomment line 31)
    my_password = 'mypassword'
    password.send_keys(my_password)
    driver.find_element_by_name("_eventId_proceed").click()

    # try checking all boxes
    try:
        # complete trojan check
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/app-root/app-consent-check/main/section/section/button"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/app-root/app-dashboard/main/div/section[1]/div[2]/button'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/app-root/app-assessment-start/main/section[1]/div[2]/button[2]'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-button-toggle-3-button"]'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-button-toggle-5-button"]'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/app-root/app-assessment-questions/main/section/section[3]/button'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-button-toggle-14-button"]'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-button-toggle-16-button"]'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-button-toggle-18-button"]'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-button-toggle-20-button"]'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-button-toggle-22-button"]'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-button-toggle-24-button"]'))).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-button-toggle-26-button"]'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/app-root/app-assessment-questions/main/section/section[8]/button'))).click()

        # click final checkbox
        checkBox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-checkbox-1-input"]')))
        ActionChains(driver).move_to_element(checkBox).click(checkBox).perform()
        # submit
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/app-root/app-assessment-review/main/section/section[11]/button'))).click()
    # run when error or already complete
    except:
        print("Trojan Check already complete or error with completing trojan check")
    finally:
        # TODO: set output to pathname of folder where you want saved image
        driver.save_screenshot("")
    # close driver
    driver.close()


job()
