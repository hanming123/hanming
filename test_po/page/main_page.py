from selenium import webdriver
from selenium.webdriver.common.by import By

from test_po.page.add_department import AddDepartmentPage
from test_po.page.add_member_page import AddMemberPage
from test_po.page.base_page import BasePage


class MainPage(BasePage):  #跳转一个主页面的类

    def goto_contact(self):  # 跳转到通讯录页面方法
        self.find(By.CSS_SELECTOR, '#menu_contacts').click() #在首页点击通讯录按钮
        return AddDepartmentPage(self.driver)  #链式调用，return到添加部门页面

    def goto_add_member(self): #跳转到添加成员页面方法
        self.driver.find_element(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()  #在首页点击添加成员按钮
        return AddMemberPage(self.driver)  #链式调用，return到添加成员页面


