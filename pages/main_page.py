from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print('Opening main page')

# locators
    products_menu_loc = "//a[@href='https://anchorlights.ru/catalog']"

# getters
    def get_products_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.products_menu_loc)))

# actions
    def open_products(self):
        self.get_products_menu().click()
        print('Going into the products menu!')
