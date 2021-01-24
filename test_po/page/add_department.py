import locator as locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_po.page.base_page import BasePage
from test_po.page.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    _username=(By.NAME,"name")
    def AddDepartment(self,name):  #添加部门
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click() #点击+号按钮
        self.find(By.CSS_SELECTOR,".js_create_party").click()  #点击添加成员按钮
        self.find(*self._username).send_keys(name) #输入部门名称
        self.find(By.CSS_SELECTOR,".js_toggle_party_list").click() #点击所属部门下拉框
        self.find(By.CSS_SELECTOR,'.qui_dialog_body.ww_dialog_body [id="1688851967256597_anchor"]').click()  #选择部门
        self.find(By.CSS_SELECTOR,"[d_ck=submit]").click() #点击确定按钮
        self.driver.refresh()
        return self

    def get_department(self):  # 获取部门信息
        locator = (By.XPATH,"//*[@class='jstree-anchor']")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(locator))  #增加显示等待，判断元素在规定的时间内是否可见
        elements = self.driver.find_elements(By.XPATH,"//*[@class='jstree-anchor']")
        # departmet_webelement_list = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-anchor jstree-clicked")
        departmet_list = []
        for element in elements:
            departmet_list.append(element.text)
        return departmet_list

    def AddDepartment_fail(self,name): #添加重复部门
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()  # 点击+号按钮
        self.find(By.CSS_SELECTOR, ".js_create_party").click()  # 点击添加成员按钮
        self.find(*self._username).send_keys(name)  # 输入部门名称
        self.find(By.CSS_SELECTOR, ".js_toggle_party_list").click()  # 点击所属部门下拉框
        self.find(By.CSS_SELECTOR, '.qui_dialog_body.ww_dialog_body [id="1688851967256597_anchor"]').click()  # 选择部门
        self.find(By.CSS_SELECTOR, "[d_ck=submit]").click()  # 点击确定按钮
        self.driver.refresh()
        return self
