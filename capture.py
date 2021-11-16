from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time

MAGICBRICKS_URL = 'https://www.magicbricks.com/'
chrome_driver_path = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"


class DataSearch:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(MAGICBRICKS_URL)

    def search(self, location, budget):
        time.sleep(3)
        rent = self.driver.find_element_by_xpath('//*[@id="tabRENT"]')
        rent.click()
        print("Rent selection success........")
        time.sleep(0.5)

        try:
            pre_load = self.driver.find_element_by_css_selector('.mb-search__input')
            pre_load.click()
            time.sleep(0.3)
            exit_pre = self.driver.find_element_by_css_selector(".mb-search__tag-close")
            exit_pre.click()
            time.sleep(0.3)

        except NoSuchElementException:
            pass
        time.sleep(0.3)
        search = self.driver.find_element_by_css_selector('.mb-search__input')
        search.send_keys(location)
        print("location input success........")
        time.sleep(0.5)
        auto_select = self.driver.find_element_by_css_selector('.mb-search__auto-suggest__item')
        auto_select.click()
        time.sleep(0.4)

        prop_type = self.driver.find_element_by_id('buy_proertyTypeDefault')
        prop_type.click()
        time.sleep(0.2)

        flat_selector = self.driver.find_element_by_xpath('//*[@id="10002_10003_10021_10022"]')
        flat_selector.click()
        time.sleep(0.2)
        bhk_2 = self.driver.find_element_by_xpath('//*[@id="11701"]')
        bhk_2.click()
        print("2Bhk select success........")
        time.sleep(0.2)

        user_budget = self.driver.find_element_by_id('rent_budget_lbl')
        user_budget.click()

        budget_max = self.driver.find_element_by_id('budgetMax')
        budget_max.click()
        time.sleep(0.4)
        budget_max.send_keys(budget)
        print("Budget input success........")
        time.sleep(0.2)

        enter = self.driver.find_element_by_xpath('//*[@id="searchFormHolderSection"]/section/div/div[1]/div[3]/div[4]')
        enter.click()
        print("Search success........")
        time.sleep(3)

        # Popup Exit >>>>>>>>>>>>>>
        try:
            exit1 = self.driver.find_element_by_xpath('//*[@id="exitIntent"]/div/div[1]')
            exit1.click()
        except NoSuchElementException:
            pass

    def get_url(self):
        url = str(self.driver.current_url)
        self.driver.quit()
        return url
