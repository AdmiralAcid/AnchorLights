from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class ProductPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        print('Opening production page')

# locators
    products_type_locs = {
        'releases' : '//a[@href="https://anchorlights.ru/categories/releases"]',
        'pre-order': '//a[@href="https://anchorlights.ru/categories/pre-order"]',
        'distribution': '//a[@href="https://anchorlights.ru/categories/distro"]',
        'tapes': '//a[@href="https://anchorlights.ru/categories/tapes"]',
        'cd': '//a[@href="https://anchorlights.ru/categories/cd"]',
        'merch': '//a[@href="https://anchorlights.ru/categories/merch"]',
        'autographs': '//a[@href="https://anchorlights.ru/categories/autographs"]',
        'rare': '//a[@href="https://anchorlights.ru/categories/rare"]',
    }
    product_name_loc = '//div[@class="products-view-name "]'
    product_add_button_loc = '//button[contains(text(), "Добавить")]'
    product_price_loc = 'price-number'
    cart_loc = '//div[@class="cart-mini"]/a'
    cart_link_loc = '//a[@href="cart"]'

# getters
    def get_product_type_obj(self, product_type):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.products_type_locs[product_type])))

    def get_products_names(self):
        return self.driver.find_elements(By.XPATH, self.product_name_loc)

    def get_product_add_buttons(self):
        return self.driver.find_elements(By.XPATH, self.product_add_button_loc)

    def get_product_prices(self):
        return self.driver.find_elements(By.CLASS_NAME, self.product_price_loc)

    def get_cart_obj(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_loc)))

    def get_cart_link_obj(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_link_loc)))

# actions
    def select_product(self, product_type):
        self.get_product_type_obj(product_type).click()
        print(f'Going into {product_type} page')

    def add_specific_product(self, product_name):
        prod_names = self.get_products_names()
        prod_buttons = self.get_product_add_buttons()
        prod_prices = self.get_product_prices()
        counter = 0
        product_found = False

        for prod_name in prod_names:
            pr_text = prod_name.text

            if pr_text == product_name:
                prod_buttons[counter].click()
                print(f'Selecting {pr_text}')
                product_found = True
                break
            else:
                counter += 1

        assert product_found == True

        return int(prod_prices[counter].text.replace(" ", ""))

    def open_shopping_cart(self):
        self.get_cart_obj().click()
        self.get_cart_link_obj().click()
        print('Opening shopping cart page')
