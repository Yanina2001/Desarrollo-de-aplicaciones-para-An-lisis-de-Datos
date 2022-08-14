from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
import time
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')
id = config['TESTING']['id']
password = config['TESTING']['password']
sitio = config['TESTING']['sitio']
friend = config['TESTING']['friend']

def fb_login(id,password,sitio):
    #opening the facebook login page
    # driver.get(sitio)
    driver.get("https://www.facebook.com/")
    driver.find_element_by_id('email').send_keys(id)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_name('login').click()

def msngr():
    #entering messenger
    redirected_url = 'https://www.facebook.com/messages/t/'
    driver.get(redirected_url)
    time.sleep(3)

def search_friend(name):
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input").send_keys(name)
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div").click()

def get_friend_messages(name):
    #j: iterates through messages
    #error: True = Msg found, False = Msg not found
    j = 1
    error = True
    #Collecting the messages
    time.sleep(3)
    #Initiating friend file
    with open(name + '.csv', 'w') as f:
        f.write('sender, message \n')
    while error:
        xpath_temp = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div[" + str(j) + "]"
        print(j)
        try:
            #Messages consists of three parts: sender, message and enter
            msg = driver.find_element_by_xpath(xpath_temp).text
            print(msg)
            #Spliting the message into three parts
            parts = msg.split('\n')
            if len(parts) == 1:
                j += 1
                continue
            #Writing messages to a file
            with open(name +'.csv', 'a') as f:
                f.write(parts[0] + ' , ' + parts[1] + '\n')
        except:
            print('No more messages')
            error = False
        j += 1


id
password
#creating driver object using Chrome
driver = webdriver.Chrome(executable_path=r"C:\\Program Files (x86)\\chromedriver.exe", options=ChromeOptions())
#maximizing the window (optional)
driver.maximize_window()
#calling the function to login
fb_login(id,password,sitio)
time.sleep(2)
#calling the function to enter messenger
msngr()
#Since the messenger is opened in a new tab, we need to switch to it
search_friend(friend)
#Getting chats count and calling the function to get messages
get_friend_messages(friend)
#Opening the file
df = pd.read_csv(friend + '.csv')
#Printing the file
print(df.head())