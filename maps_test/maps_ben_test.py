import pytest
from selenium import webdriver

from maps_page.maps_ben_page import BenefitPage


class TestBenefit:
    @pytest.fixture
    def setup(self):
        global driver
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.moneyhelper.org.uk/en')
        print(self.driver.title)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        yield
        self.driver.quit()

    def test_cookie(self, setup):
        self.cookie_ben = BenefitPage(self.driver)
        self.cookie_ben.cookie()




