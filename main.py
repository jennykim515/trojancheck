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


def job(u, p):
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
    username.send_keys(u)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))

    password = driver.find_element_by_id('password')
    password.clear()
    password.send_keys(p)
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
        barcode = driver.find_element_by_xpath("/html/body/app-root/app-dashboard/main/div/section[1]/div/div[2]")
        barcode.screenshot('')
    # close driver
    driver.close()



# automated email sending with image attachment
def send_email(receiver_email, u, p):
    job(u, p)
    subject = "Trojan Check"
    body = "Good morning! This is an automated message with your trojan check."
    sender_email = ""  # robot email - set account to less secure
    password = ""  

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "trojancheck.png"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
   

def main():
    # TODO: Define email information
    receiver_email = ""
    username = ""
    password = ""
    send_email(receiver_email, username, password)
