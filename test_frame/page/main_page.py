from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.addresslist_Page import AddressListPage


class MainPage(BasePage):  #主页面
    def goto_addresslist_page(self):
        self.find_and_click((By.XPATH,"//*[@resource-id='com.tencent.wework:id/eim']"))  #点击其它企业按钮
        self.find_and_click((By.XPATH,"//*[@text='通讯录']"))
        return AddressListPage(self.driver)  #跳转到通讯录的添加成员页面
