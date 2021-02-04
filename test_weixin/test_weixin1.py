from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo():

  def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        # "appActivity": ".view.WelcomeActivityAlias",
        desired_caps['noReset'] = 'true'  # 此项的意思为，1,当界面有弹框，关闭界面，当再次打开应用时，弹框会消失
                                          # 2,是否在测试前后重置相关环境（例如首次打开弹框，参考第一条注释，或者是登录信息）
        desired_caps['dontStopAppOnReset'] = "true"  # 首次启动App的时候，不停止App(可以调试或者运行的时候提升运行速度)
        desired_caps['skipDeviceInitialization'] = "true"  # 跳过安装，权限设置等操作(可以调试或者运行的时候提升运行速度)
        desired_caps['unicodeKeyBoard']='true' #设置输入框可以进行中文输入
        desired_caps['resetKeyBoard']='true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(30)

  def teartown(self):
        self.driver.quit()

  def test_add_member(self):
        name = "张三"
        gender = "女"
        phonenum = '18200000001'
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()  # 滚动查找 ,固定写法，只需更改text里面的值即可
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="男"]').click()
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()

        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fuy").send_keys(phonenum)
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/ie7').click()
        ele=self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text
        assert "添加成功" == ele