import requests


def test_add_member():
    # 获取token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2d33eed4bd12c5b2&corpsecret=RqXmfK2UC-9ntKjtJU7jPPcDdoHV0zdy5rdtsZRsdI4"
    r = requests.get(url)
    token = r.json()['access_token']

    # 数据清理（删除成员）
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=aibeibei"
    r = requests.get(url)
    print(r.json())

    # 创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
            "userid": "aibeibei",
            "name": "爱贝贝",
            "department": [1],
            "mobile": "+86 13800000088",
            }
    r = requests.post(url,json=body)
    # print(r.json())

    # 读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=1589968"
    r = requests.get(url)
    print(r.json())


def test_delete_member():
    # 获取token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2d33eed4bd12c5b2&corpsecret=RqXmfK2UC-9ntKjtJU7jPPcDdoHV0zdy5rdtsZRsdI4"
    r = requests.get(url)
    token = r.json()['access_token']

    # 数据清理（数据准备：创建成员）
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "aibeibei",
        "name": "爱贝贝",
        "department": [1],
        "mobile": "+86 13800000088",
    }
    r = requests.post(url, json=body)
    print(r.json())

    # 删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=aibeibei"
    r = requests.get(url)
    print(r.json())

    # 读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=1589968"
    r = requests.get(url)
    print(r.json())


