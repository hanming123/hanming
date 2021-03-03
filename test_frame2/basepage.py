import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from test_frame2.handle_black import handle_black


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    @handle_black
    def find(self,locator):
        return self.driver.find_element(*locator)

    def find_and_click(self,locator): #查找并点击
        self.find(locator).click()

    def find_and_text(self,locator,text): #查找并且输入
        self.find(locator).send_keys(text)
    def send(self,locator,content):
        self.find(locator).send_keys(content)

    def scroll_find_click(self,text):  #滑动查找
        element=(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));')  # 滚动查找 ,固定写法，只需更改text里面的值即可
        self.find_and_click(element)

    def find_and_get_text(self,locator):
        return self.find(locator).text

    def run_steps(self,page_path, operation):
        with open(page_path,'r',encoding="utf-8") as f:
            data = yaml.safe_load(f)
        # 支持 po下多个操作
        steps = data[operation]
        for step in steps:
            action = step['action']
            if action == "find_and_click":
                self.find_and_click(step['locator'])
            elif action == "send":
                self.send(step['locator'],step['content'])