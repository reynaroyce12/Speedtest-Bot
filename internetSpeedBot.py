# import os
import os
import time
from smtplib import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

driver_path = os.getenv('DRIVER_PATH')
my_email = os.getenv('MY_EMAIL')
password = os.getenv('PASSWORD')


class InternetSpeed:
    def __init__(self):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        item_url = 'https://www.speedtest.net/'
        self.driver.get(item_url)
        self.up_speed = 80
        self.down_speed = 60

    def send_mail(self, current_down, current_up):
        if current_down < self.down_speed or current_up < self.up_speed:
            with SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs="roycereyna12@gmail.com",
                                    msg=f"Subject:Customer Complaint 📝\n\n"
                                        f"Hello Internet Provider,Why is my internet "
                                        f"speed {current_down}Down/{current_up}Up when I pay for {self.down_speed}Down/"
                                        f"{self.up_speed}Up.".encode('utf-8'))

    def speedChecker(self):
        time.sleep(20)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                       'div[1]/a/span[4]')
        go_button.click()
        time.sleep(40)

        current_down = self.driver.find_element(By.XPATH,
                                                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div'
                                                '[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        current_up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div'
                                                        '[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')

        float_down = float(current_down.text)
        float_up = float(current_up.text)
        self.send_mail(float_down, float_up)
