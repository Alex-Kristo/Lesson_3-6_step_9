class TestMainPage(object):
    def test_basket_presence(self, driver):
        driver.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        basket_selector = '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'
        driver.find_element_by_xpath(basket_selector)
