import sys
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from base.base_class import Base

MODIFIER = Keys.COMMAND if sys.platform == "darwin" else Keys.CONTROL

class Filter(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # need to find colors
        if self.check_filters_enabled():
            # open colors block
            self.open_colors_spoiler()
            # getting colors as DOM objs
            color_objs = driver.find_elements(By.XPATH,
                                              '/html/body/div[6]/main/div/div[2]/div[2]/article/div/form/div[2]/div/div[2]/div/div/div[1]/div/div/div')
            # stuff them into dictionary
            for color_obj in color_objs:
                self.colors[color_obj.get_attribute("title")] = color_obj

        # need to collect sort options
        if self.check_filters_enabled():
            sort_opts = driver.find_elements(By.XPATH, '//*[@id="Sorting"]/option')
            for sort_opt in sort_opts:
                self.sort_options.append(sort_opt.text)

# locators
    filters_title_loc = '/html/body/div[6]/main/div/div[2]/div[2]/article/div/div[1]'
    min_price_loc = '//input[@name="filteredModelMin"]'
    max_price_loc = '//input[@name="filteredModelMax"]'
    colors_more_loc = '//span[@data-ng-switch-when="true"]'
    confirm_button_loc = '//input[@value="Применить"]'
    sorting_loc = '//select[@name="Sorting"]'
    sort_option_loc = '//*[@id="Sorting"]/option'
    colors = {}
    sort_options = []

# actions
    def check_filters_enabled(self):
        filter_title = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.filters_title_loc)))
        filter_text = filter_title.text
        print(f'filter_text is {filter_text}')
        assert filter_text == 'ФИЛЬТРЫ'
        return True

    def get_more_colors_spoiler(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.colors_more_loc)))

    def get_color_obj(self, color):
        if color not in self.colors:
            assert False
        return self.colors[color]

    def get_min_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.min_price_loc)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.max_price_loc)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button_loc)))

    def get_sort_select(self):
        return Select(self.driver.find_element(By.XPATH, self.sorting_loc))

    def open_colors_spoiler(self):
        self.get_more_colors_spoiler().click()
        print('Getting colors')

    def select_color(self, color):
        self.get_color_obj(color).click()
        print(f'Selecting "{color}" color')

    def enter_min_price(self, min_price):
        self.get_min_price().send_keys(Keys.BACKSPACE * 4)
        self.get_min_price().send_keys(min_price)
        print(f'Entering min_price {min_price}')

    def enter_max_price(self, max_price):
        self.get_max_price().send_keys(Keys.BACKSPACE * 4)
        self.get_max_price().send_keys(max_price)
        print(f'Entering max_price {max_price}')

    def press_confirm(self):
        self.get_confirm_button().click()
        print('Confirm filter')

    def select_sorting(self, option):
        if option not in self.sort_options:
            assert False
        self.get_sort_select().select_by_visible_text(option)
        print(f'Selecting "{option}" sorting option')
