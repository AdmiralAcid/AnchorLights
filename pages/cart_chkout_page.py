import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Checkout(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# locators
    cart_chkout_button_loc = '//a[@data-ng-href="checkout"]'
    item_name_loc = 'cart-full-name-link'
    email_input_loc = '//input[@autocomplete="email"]'
    name_input_loc = '//input[@autocomplete="given-name"]'
    surname_input_loc = '//input[@autocomplete="family-name"]'
    patronym_input_loc = '//input[@autocomplete="additional-name"]'
    phone_input_loc = '//input[@autocomplete="tel"]'
    radio_sdek_base_opt_loc = '//span[@class="shipping-item-radio"]'
    address_input_loc = '//input[@autocomplete="shipping street-address"]'
    delievery_cost_loc = '//div[@data-ng-bind="checkout.Cart.Delivery"]'
    final_price_loc = '/html/body/div[6]/main/div/div[2]/div[2]/div[1]/form/div[2]/div[1]/span'
    approve_button_loc = '//div[@class="checkout-summary__btn-submit-wrap"]/button'

# getters
    def get_cart_chkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_chkout_button_loc)))

    def get_item_obj(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME , self.item_name_loc)))

    def get_email_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_input_loc)))

    def get_name_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name_input_loc)))

    def get_surname_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.surname_input_loc)))

    def get_patronym_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.patronym_input_loc)))

    def get_phone_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone_input_loc)))

    def get_address_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.address_input_loc)))

    def get_approve_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.approve_button_loc)))

    def get_sdek_base_opt(self):
        needs_address = False
        radio_opts = self.driver.find_elements(By.XPATH, self.radio_sdek_base_opt_loc)
        if len(radio_opts) == 3:
            return radio_opts[1], needs_address
        else:
            needs_address = True
            return radio_opts[0], needs_address

    def get_delievery_price(self):
        del_price_obj = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.delievery_cost_loc)))
        delievery_text = del_price_obj.text
        if delievery_text == 'Бесплатно':
            return 0
        return int(delievery_text.split(' ')[0])

    def get_final_price(self):
        final_price = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.final_price_loc)))
        final_price_text = final_price.text
        return int(final_price_text[:final_price_text.find('р')].replace(' ', ''))

# actions
    def check_item_name(self, item_name):
        item_obj_name = self.get_item_obj().text
        return item_obj_name == item_name

    def open_cart_chkout(self):
        self.get_cart_chkout().click()
        print('Going to checkout page')

    def fill_email_input(self, email):
        self.get_email_input().click()
        self.get_email_input().send_keys(email)
        print(f'Email: {email}')

    def fill_name_input(self, name):
        self.get_name_input().click()
        self.get_name_input().send_keys(name)
        print(f'Name: {name}')

    def fill_surname_input(self, surname):
        self.get_surname_input().click()
        self.get_surname_input().send_keys(surname)
        print(f'Surname: {surname}')

    def fill_patronym_input(self, patronym):
        self.get_patronym_input().click()
        self.get_patronym_input().send_keys(patronym)
        print(f'Patronym: {patronym}')

    def fill_phone_input(self, phone):
        self.get_phone_input().click()
        self.get_phone_input().send_keys(phone)
        print(f'Phone: {phone}')

    def fill_address_input(self, address):
        self.get_address_input().click()
        self.get_address_input().send_keys(address)

    def select_sdek_base_radio(self):
        delievery_opt, need_address = self.get_sdek_base_opt()
        delievery_opt.click()
        return need_address

    def fill_in_checkout_info(self, email, name, surname, patronym, phone, address):
        print('Filling in checkout info')
        self.fill_email_input(email)
        self.fill_name_input(name)
        self.fill_surname_input(surname)
        self.fill_patronym_input(patronym)
        self.fill_phone_input(phone)
        self.driver.execute_script("window.scrollTo(0, 500);")
        needs_address = self.select_sdek_base_radio()
        if needs_address:
            self.fill_address_input(address)

    def finalize(self):
        self.get_approve_button().click()