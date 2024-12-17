from selenium import webdriver


class WebDriverSetup:
    def __init__(self, browser):
        self.browser = browser
        self.driver = None

    def start_driver(self):
        if self.browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif self.browser.lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif self.browser.lower() == "edge":
            self.driver = webdriver.Edge()

        return self.driver
    
    def quit_driver(self):
        if self.driver:
            self.driver.quit()
    