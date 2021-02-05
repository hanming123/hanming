from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import BasePage
from test_appium.page.contactedit_page import ContactEditPage

#点击手动添加
class MemberInvitePage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def addconect_menual(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click() #普通写法

        self.find_and_click((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
        return ContactEditPage(self.driver)

    def get_toast(self):
        # ele = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text #普通用法

        ele = self.find_and_get_text((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        return ele