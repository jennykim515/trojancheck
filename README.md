# trojancheck
## Description
This program automates the wellness exam that is needed to access campus and activities for USC students. Please make sure that you meet all of the requirements of the wellness exam before submitting the Trojan Check. 

## How to Use
### Create Workspace
Create a folder where the program will run and store images. Take note of its path name.  

### Installing ChromeDriver
Webdriver allows automated navigation of web pages. There are different Webdrivers for different web browsers, but this program only works for Chrome browser.

Download the chrome driver here: https://chromedriver.chromium.org/downloads

Put the chrome driver in the source folder.

### TODO
#### job function
On line 23, specify the path to the chrome driver. 

#### main
In the main file, fill in all information under TODO. This includes USC id, USC password, and an email account

#### send_email
This section is code extracted from: https://docs.python.org/3/library/email.examples.html. 

Use the link to set up an email that will be sending emails automatically. The sender email and password information should be then filled in.

## Run Program    
Running the program should result in an automated Trojan Check. Check the receiver email's inbox for a screenshot of the barcode and current weather information.

## Future Work
So far, the Trojan Check only works if manually ran by the user every day. However, cron can be used to automate tasks on a computer so that a program can run at customized times of the day, week, or month. While straightforward for most programs, cron experiences bugs when trying to access the internet and web browser from an asleep computer, which is when we'd want to run the program. 

Once a solution is found, I will update the repository with more information.
