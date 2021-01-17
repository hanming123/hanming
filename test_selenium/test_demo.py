import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestTestweixin():
    def setup_method(self):
        # self.driver = webdriver.Chrome()
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_cookie(self):
        # print(self.driver.get_cookies())  #获取cookie
        # cookies = self.driver.get_cookies()
        # with open("cookie.json","w") as f :  #以文件流的形式打开文件
        #     json.dump(cookies,f)  # #存储cookie到cookie.json

        self.driver.get("https://work.weixin.qq.com/")

        with open("cookie.json","r") as f: #以文件流的形式打开文件
            cookies = json.load(f)  #读取cookie
        # print(cookies)
        for cookie in cookies:  #注入cookies
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        sleep(5)
        self.driver.find_element(By.ID,"menu_customer").click()
        sleep(5)
        self.driver.close()

    # def test_testweixin(self):
    #     self.driver.get("https://work.weixin.qq.com/")
    #     sleep(15)
    #     self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()
    #     self.driver.find_element(By.XPATH,"//*[@id='menu_customer']").click()
    #     self.driver.find_element(By.ID,"kw").send_keys(Keys.ENTER)
        # sleep(5)
        # self.driver.close()
