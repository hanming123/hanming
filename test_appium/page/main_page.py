from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.aaddresslist_page import AddresslistPage

# 点击通讯录
from test_appium.page.basepage import BasePage


class MainPage(BasePage): #主页的类
    # def __init__(self,driver):
    #     self.driver = driver
    def click_addresslist(self):  # 创建添加成员方法

        # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()  #普通用法

        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return AddresslistPage(self.driver)  #跳转到添加成员页面

