import pytest
import yaml

from test_pytest.pythoncode.calculator import Calculator


def get_data():
    with open("./task.yml") as f:
        a=yaml.safe_load(f)
        adds = a["adds"]
        idsa = a["idsa"]
        sub = a["sub"]
        idsb = a["idsb"]
        mul = a["mul"]
        idsc = a["idsc"]
        div = a["div"]
        idsd = a["idsd"]
        return [adds,idsa,sub,idsb,mul,idsc,div.idsd]
class Tset_Calc:
    def setup_calss(self):
        print("开始验证")
    def teardown_calss(self):
        print("结束验证")
    def setup(self):
        print("开始计算")
        self.cal = Calculator
    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize(["a","b","expect"],get_data()[0],ids=get_data()[1])
    def test_add(self,a,b,expect):
        add = self.cal.add(a,b)
        print(add)
        assert add == expect

    @pytest.mark.parametrize(["a","b","expect"],get_data()[2],ids=get_data()[3])
    def test_sub(self,a,b,expect):
        sub = self.cal.sub(a,b)
        print(sub)
        assert sub == expect

    @pytest.mark.parametrize(["a","b","expect"],get_data()[4],ids=get_data()[5])
    def test_mul(self,a,b,expect):
        mul = self.cal.mul(a,b)
        print(mul)
        assert mul == expect

    @pytest.mark.parametrize(["a","b","expect"],get_data()[6],ids=get_data()[7])
    def test_div(self,a,b,expect):
        div = self.cal.div(a,b)
        print(div)
        assert div == expect

if __name__ == '__main__':
    pytest.main()



