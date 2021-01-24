from test_po.page.main_page import MainPage


class TestAddDepartment:
    def setup(self):
        self.mainpage = MainPage()
    def teardown(self):
        self.mainpage.driver.quit()
    def test_department(self):
        #1,首页跳转到通讯录页面  2，添加部门  3，获取部门信息
        result = self.mainpage.goto_contact().AddDepartment("测试部").get_department()
        assert "测试部" in result

        # 1,首页跳转到通讯录页面  2，添加部门  3，获取部门信息
    def test_department_file(self):
        result = self.mainpage.goto_contact().AddDepartment_fail("测试部").get_department()
        assert "测试部" not in result