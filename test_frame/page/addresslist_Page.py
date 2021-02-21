from selenium.webdriver.common.by import By

from test_frame.basepage import BasePage
from test_frame.page.memberInvite_page import MemberInvitePage


class AddressListPage(BasePage): #添加成员
    def goto_add_member(self):
        self.find_and_click((By.XPATH,"//*[@text='添加成员']")) #点击添加成员按钮
        return MemberInvitePage(self.driver)

