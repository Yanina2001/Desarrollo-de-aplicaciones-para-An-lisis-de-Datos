from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import subdriver
import time

id = "tucorreo@gmail.com"
password= "PruebaSelenium1"

# usr=input('Enter Email Id:')
# pwd=input('Enter Password:')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
print ("Opened facebook")
# sleep(1)

# Interactivo 
# username_box = driver.find_element_by_id('email')
# username_box.send_keys(usr)

# Manual 
print ("Email Id entered")
# sleep(1)

# Interactivo 
# password_box = driver.find_element_by_id('pass')
# password_box.send_keys(pwd)

# Manual
print ("Password entered")


driver.find_element_by_id('email').send_keys(id)
driver.find_element_by_id('pass').send_keys(password)

# login_box = driver.find_element_by_id('u_0_d_q5')
login_box = driver.find_element_by_name('login')
login_box.click()

time.sleep(5)

boton = driver.find_element(by=By.CSS_SELECTOR, value='i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3 s45kfl79 emlxlaya bkmhp75w spb7xbtv')
boton.click()

time.sleep(5)

# mensaje = driver.find_element(by=By.CLASS_NAME, value='i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s rnr61an3 s45kfl79 emlxlaya bkmhp75w spb7xbtv')
# mensaje.click()




# print ("Done")
# input('Press anything to quit')
# driver.quit()
# print("Finished")
