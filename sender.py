from selenium import webdriver

import time

chrome_driver_path = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"


class SendData:
    def __init__(self, sheet_url):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(sheet_url)
        time.sleep(2)

    def send_address(self, address):
        data_line1 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        data_line1.click()
        data_line1.send_keys(address)

    def send_price(self, price):
        data_line2 = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        data_line2.click()
        data_line2.send_keys(price)

    def send(self):
        send = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        send.click()
        # time.sleep(0.2)
        next_resp = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        next_resp.click()
        time.sleep(0.2)
