from appium import webdriver

from test_appium.page.basepage import BasePage
from test_frame.page.main_page import MainPage


class App(BasePage):
    def start(self): #启动APP
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps['autoGrantPermissions'] = True  # 自动点掉弹框
            desired_caps['dontStopAppOnReset'] = True  #不停止App,继续运行
            # "appActivity": ".view.WelcomeActivityAlias",
            desired_caps['noReset'] = 'true'  # 此项的意思为，1,当界面有弹框，关闭界面，当再次打开应用时，弹框会消失
                                              # 2,是否在测试前后重置相关环境（例如首次打开弹框，参考第一条注释，或者是登录信息）
            # desired_caps['dontStopAppOnReset'] = "true"  # 首次启动App的时候，不停止App(可以调试或者运行的时候提升运行速度)
            desired_caps['skipDeviceInitialization'] = "true"  # 跳过安装，权限设置等操作(可以调试或者运行的时候提升运行速度)
            desired_caps['unicodeKeyBoard'] = 'true'  # 设置输入框可以进行中文输入
            desired_caps['resetKeyBoard'] = 'true'
            desired_caps['newCommandTimeout'] = 300
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(80)
        else:
            self.driver.launch_app()
        return self

    def restart(self): #重启App
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):  #关闭App
        self.driver.quit()
        return self

    def goto_main(self)->MainPage: #定义进入页面
        return MainPage(self.driver)  #跳转到主页面
