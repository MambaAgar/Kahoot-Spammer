from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import threading
import time
import os

# Getting pin number
pin = str(input("Enter the Kahoot's Pin Number: "))
# Getting base name
name = str(input("Enter your base name: "))
# Getting number of bots wanted
number_of_bots = int(input("Enter the number of bots you want: "))
# Counter
counter = 0
# Number added onto end of base name due to Kahoot not accepting same names
name_num = 1
#driver global for break_out()
drivers = []

def joinKahoot(pin, name):
    global drivers
    driver = webdriver.PhantomJS(executable_path=r"phantomjs-2.1.1-windows\bin\phantomjs.exe", service_log_path = os.path.devnull)
    drivers.append(driver)
    driver.get("https://kahoot.it/#/")

    #Fill out and submit pin
    time.sleep(1)
    element = driver.find_element_by_id("inputSession")
    element.send_keys(pin)
    element.submit()

    #Fill out and submit username
    time.sleep(1)
    element = driver.find_element_by_id("username")
    element.send_keys(name)
    element.submit()

def start_joinKahoot(name):
    t = threading.Thread(target=joinKahoot, args=(pin,name))
    t.daemon = True
    t.start()

def break_out():
        break_out = str(input("Enter L to Disconnect: "))
        if break_out.lower() == "l":
            for d in drivers:
                d.quit()
        elif break_out.lower()!= "l":
            print("Enter L to Disconnect: ")
            
# Main ignition
if __name__ == "__main__":
    for x in range(0, number_of_bots):
        name_num += 1
        start_joinKahoot(name = "{}{}".format(name, name_num))
        time.sleep(1)
    print("Leave python running to keep the kahoot accounts in. Press L to Exit.")
    break_out()
    




