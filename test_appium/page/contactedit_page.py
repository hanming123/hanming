from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.basepage import BasePage

#编辑成员的信息
class ContactEditPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def edit_name(self,name):
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        # self.find_and_text()
        return self

    def edit_gender(self,gender):
        locator = (MobileBy.XPATH, '//*[@text="男"]')
        ele = WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        # gender = "男"
        if gender == '女':

            # self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click() #普通写法
            self.find_and_click((MobileBy.XPATH,'//*[@text="女"]'))
        else:
            # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click() #普通写法
            self.find_and_click((MobileBy.XPATH, '//*[@text="男"]'))
        return self

    def edit_phonenum(self,phonenum):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fuy").send_keys(phonenum)
        return self

    def click_save(self):  #保存
        from test_appium.page.memberinvit_Page import MemberInvitePage  #这里是局部引用导入的包，因为语法上重复导包是不行的
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ie7').click() #普通用法
        self.find((MobileBy.ID, 'com.tencent.wework:id/ie7')).click()
        return MemberInvitePage(self.driver)


