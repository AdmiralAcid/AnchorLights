from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Initial(Base):

    url = 'https://anchorlights.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print('Initiating...')

# locators
    piter_yes_loc = '//button[@data-ng-click="zonePopover.zoneOk()"]'

# getters
    def get_piter_yes(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.piter_yes_loc)))

# actions
    def set_piter(self):
        self.get_piter_yes().click()

    def preauth(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        print(self.get_url())
        self.set_piter()
