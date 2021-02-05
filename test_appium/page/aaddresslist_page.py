from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.basepage import BasePage
from test_appium.page.memberinvit_Page import MemberInvitePage

# 点击添加成员
class AddresslistPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def add_member(self): #定义添加成员方法
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                         'new UiScrollable(new UiSelector().'
        #                         'scrollable(true).instance(0)).'
        #                         'scrollIntoView(new UiSelector().'
        #                         'text("添加成员").instance(0));').click()  # 滚动查找 ,固定写法，只需更改text里面的值即可
        self.scroll_find_click("添加成员")
        return MemberInvitePage(self.driver)  #跳转到手动输入添加成员页面