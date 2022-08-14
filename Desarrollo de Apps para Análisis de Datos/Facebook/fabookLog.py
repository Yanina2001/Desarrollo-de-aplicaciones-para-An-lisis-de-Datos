from selenium import webdriver
import time
import re

def fb_login(id,password):
    #opening the facebook login page
    driver.get("https://www.facebook.com/")
    driver.find_element_by_id('email').send_keys(id)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_name('login').click()

def msngr():
    #entering messenger
    redirected_url = 'https://www.facebook.com/messages/t/'
    driver.get(redirected_url)
    time.sleep(3)

def chat_counter():
    # Implementation using selenium
    i = 1
    error = True
    while error:
      try:
          chat_section = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[" + str(i) + "]")
      except:
          print('No more chats')
          error = False
      i += 1
    return i - 1
       
def get_messages(chats):
    for i in range(1, chats + 1):
        #i: iterates through the chats
        #j: iterates through messages
        #error: True = Msg found, False = Msg not found
        j = 1
        error = True
        #Selecting the chat
        xpath = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[" + str(i) + "]"
        driver.find_element_by_xpath(xpath).click()
        #Getting friend's name
        friend_name = driver.find_element_by_xpath(xpath).text.split('\n')[0]
        #Collecting the messages
        time.sleep(3)
        #Initiating friend file
        with open(friend_name + '.txt', 'w') as f:
            f.write('Conversacion con ' + friend_name + '\n')
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
                with open(friend_name +'.txt', 'a') as f:
                    f.write(parts[0] + ': ' + parts[1] + '\n')
            except:
                print('No more messages')
                error = False
            j += 1

#user credentials
id = "tucorreo@gmail.com"
password= "PruebaSelenium1"
#creating driver object using Chrome
driver = webdriver.Chrome(executable_path=r"C:\\Program Files (x86)\\chromedriver.exe")
#maximizing the window (optional)
driver.maximize_window()
#calling the function to login
fb_login(id,password)
time.sleep(2)
#calling the function to enter messenger
msngr()
#Getting chats count and calling the function to get messages
get_messages(chat_counter())

# scroll down, page down, mover la barra lateral de scroll, identificar cuando llegue al final de la pagina
# limitar numero de mensajes, solo mensaje de amigos, los dos, por horario, etc
# hora, quien lo envie y texto
