import configparser
#from selenium import webdriver
from time import sleep
from webbot import Browser

consoles = {
    "ps5": "https://www.walmart.com/ip/PlayStation-5-Console/363472942",
    "ps5_digital": "https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815",
    "xbox": "https://www.walmart.com/ip/XB1-Xbox-Series-X/443574645"
}

retailers = {
    "wm_home": "https://www.walmart.com/",
}

class WMProcess():
    """
    Walmart login credentials/process
    """
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("../configs/credentials.conf")
        #setup login and site information
        self.username = config['creds']['username']
        self.pw = config['creds']['pw']
        self.site = retailers['wm_home']
        self.ps5 = consoles['ps5']
        self.ps5_digital = consoles['ps5_digital']
        self.xbox = consoles['xbox']
        self.web = Browser()

    def open_browser(self):
        #gc = webdriver.Chrome(r"../configs/drivers/chromedriver_win32/chromedriver.exe")
        #gc.get(self.site)
        self.web.go_to(self.site)
        sleep(2)


    def login(self):
        self.web.click('Account')
        self.web.click('Sign In')
        self.web.type(self.username, into='email')
        self.web.type(self.pw, into='password')
        self.web.click('Sign In')
        self.web.go_to(self.xbox)

    def add_to_cart(self):
        pass

    def checkout(self):
        pass

    def delivery(self):
        pass

    def confirm_address(self):
        pass

    def select_payment(self):
        pass

    def review_order(self):
        pass

    def main(self):
        self.open_browser()


if __name__ == '__main__':
    get_console = WMProcess()
    get_console.open_browser()
    get_console.login()
    sleep(5)