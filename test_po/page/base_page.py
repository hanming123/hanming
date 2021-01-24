import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
class BasePage: #公共类用于继承 封装了cookie登录，元素定位
    def __init__(self,base_driver=None):
        base_driver:WebDriver
        if base_driver is None:
           self.driver = webdriver.Chrome()
           self.driver.implicitly_wait(10)  #添加一个隐式等待
        # self.driver.find_element(By.CSS_SELECTOR, "。ww_indexImg_AddMember").click()
           self._cookie_login()
        else:
            self.driver = base_driver

    def _cookie_login(self):   #cookie登录
        self.driver.get("https://work.weixin.qq.com/")
        with open("../tastcases/cookie.json", "r") as f:  # 以文件流的形式打开文件
            cookies = json.load(f)  # 读取cookie
        # print(cookies)
        for cookie in cookies:  # 注入cookies
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        # sleep(5)
        # self.driver.find_element(By.ID, "menu_customer").click()
        # # sleep(5)
        # # self.driver.close()
    #封装元素定位
    def find(self,by,value):
        return self.driver.find_element(by=by,value=value)
