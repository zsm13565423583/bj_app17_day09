from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def search_ele(self, loc, timeout=5, poll=1):

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1):

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1):

        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=1):

        # 定位
        input_text = self.search_ele(loc, timeout, poll)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)
