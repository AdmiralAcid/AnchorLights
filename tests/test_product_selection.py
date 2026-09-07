import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from base.base_class import Base
from pages.cart_chkout_page import Checkout
from pages.filters import Filter
from pages.initial import Initial
from pages.main_page import MainPage
from pages.production_page import ProductPage

#options
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--guest')

# driver stuff
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

def test_amur_fishes():
    artist_name = 'Олег Лёгкий'
    auth = Initial(driver)
    main = MainPage(driver)
    product = ProductPage(driver)

    auth.preauth()
    time.sleep(2)
    main.open_products()
    product.select_product('distribution')
    # filtering and sorting
    ffilter = Filter(driver)
    ffilter.enter_min_price('2000')
    ffilter.enter_max_price('3000')
    time.sleep(2)
    ffilter.select_color('Черный')
    time.sleep(1)
    ffilter.press_confirm()
    ffilter.select_sorting('Названию, по убыванию')

    # adding Amur Fishes album
    fishes_price = product.add_specific_product(artist_name.upper()) # how much is the fish?
    # going into shopping cart
    time.sleep(5)
    product.open_shopping_cart()
    time.sleep(2)
    checkout = Checkout(driver)
    assert checkout.check_item_name(artist_name)
    # going into checkout page
    checkout.open_cart_chkout()
    checkout.fill_in_checkout_info('johndoe@never.com',
                                   'Иован',
                                   'Петров',
                                   'Ионович',
                                   '9999999999',
                                   'Москва, ул. Пушкина, д. Колотушкина')
    delievery_price = checkout.get_delievery_price()
    driver.execute_script("window.scrollTo(0, 800);")
    final_price = checkout.get_final_price()
    assert final_price == delievery_price + fishes_price
    print(f'Be ready to pay {fishes_price} + {delievery_price} = {final_price}')
    # not going to press 'approve' as it will place a real order and real business will get a false signal
    # checkout.finalize()
