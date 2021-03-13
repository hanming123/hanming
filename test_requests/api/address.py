import requests

from test_requests.api.base import Base


class Address(Base):
    def add_member(self, userid: str, name: str, mobile: str, department: list, **kwargs):  #创建成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
        }
        body.update(kwargs)
        return self.send("post", url, json=body)

        # r = requests.post(url, json=body) #未封装Base 的写法
        # return r.json()

    def get_member(self, userid: str):   #查询成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send("get", url)

        # r = requests.get(url)  #未封装Base 的写法
        # return r.json()

    def update_member(self,userid: str, name: str, **kwargs):  #更新成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name,
        }
        body.update(kwargs)
        return self.send("post", url, json=body)

        # r = requests.post(url, json=body) #未封装Base 的写法
        # return r.json()

    def delete_member(self,userid: str):  #删除成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send("get", url)

        # r = requests.get(url) #未封装Base 的写法
        # return r.json()


