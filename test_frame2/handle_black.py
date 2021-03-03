from selenium.webdriver.common.by import By

def handle_black(fun):
    def run(*args,**kwargs):
        instance = args[0]
        black_lists = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
        try:
           return fun(*args,**kwargs)
        except Exception as e :
            for black in black_lists:
                eles = instance.driver.find_elements(*black)
                if len(eles) > 0 :
                    eles[0].click()
                    return fun(*args,**kwargs)
            raise e
    return run