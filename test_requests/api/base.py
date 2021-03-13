import requests


class Base:
    def __init__(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2d33eed4bd12c5b2&corpsecret=RqXmfK2UC-9ntKjtJU7jPPcDdoHV0zdy5rdtsZRsdI4"
        r = requests.get(url).json()
        self.token = r['access_token']
        #声明一个session
        self.s = requests.Session()
        #把token放入到session，每次参数都有token
        self.s.params = {'access_token':self.token}

    def send(self, *args, **kwargs):
        r = self.s.request(*args , **kwargs)
        return r.json()