import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self):
        curr_url = self.driver.current_url
        return curr_url

    def assert_word(self, lword, rword):
        ltext = lword.text
        assert ltext == rword
        print('Passed')

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
        screen_name = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\satur\\PycharmProjects\\AnchorLights\\screens\\' + screen_name)

    def assert_url(self, url):
        curr_url = self.driver.current_url
        assert curr_url == url
        print('URL is right')
