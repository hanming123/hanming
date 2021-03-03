import yaml
from selenium.webdriver.common.by import By

from test_frame2.basepage import BasePage
from test_frame2.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):

        # 没有做封装到basepage页面时的写法
        # with open("../page/market_page.yaml",'r',encoding="utf-8") as f:
        #     data = yaml.safe_load(f)
        # for step in data:
        #     action = step['action']
        #     if action == "find_and_click":
        #         self.find_and_click(step['locator'])
        self.run_steps("../page/market_page.yaml","goto_search")
        # self.find_and_click((By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)