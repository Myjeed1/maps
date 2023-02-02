import time

from selenium.webdriver.common.by import By

from maps_loc.maps_location import LocatorBenefit


class BenefitPage:
    def __init__(self, driver):
        self.driver = driver

    def cookie(self):
        self.driver.find_element(By.XPATH, LocatorBenefit.cookie1).click()
        time.sleep(5)
