import pytest

from test_requests.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()  #实例化类

    @pytest.mark.parametrize("userid, mobile", [("woaibeibei123","13699999999"),
                                                ("woaibeibei456", "13699999988"),
                                                ("woaibeibei789", "13699998787")])
    def test_add_member(self, userid, mobile):
        name = "我爱贝贝呀"
        department = [1]
        # 数据清理（删除成员）
        self.address.delete_member(userid)

        #创建成员
        r = self.address.add_member(userid=userid, name=name, mobile=mobile, department=department)
        assert r.get("errcode") == 0
        assert r.get("errmsg") == "created"
        #查询结果
        r = self.address.get_member(userid)
        assert r.get("name","userid 添加失败") == name


