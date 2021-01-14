import os
import pytest
import yaml

from test_pytest.pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def get_calc():
    calc = Calculator()
    return calc

file_name = os.path.dirname(__file__)+'/task.yml'

with open(file_name) as f :
    datas = yaml.safe_load(f)
    print(datas)
    add_datas = datas["adds"]
    add_ids = datas["idsa"]
    sub_datas = datas["sub"]
    sub_ids = datas["idsb"]
    mul_datas = datas["mul"]
    mul_ids = datas["idsc"]
    div_datas = datas["div"]
    div_ids = datas["idsd"]

# @pytest.fixture(scope="module")
# def start_end():
#     print("开始计算")
#     yield
#     print("结束计算")

@pytest.fixture(scope="module",params=add_datas,ids=add_ids)
def get_datas_add(request):
    print("开始计算")
    datas = request.param
    yield datas

@pytest.fixture(scope="module",params=sub_datas,ids=sub_ids)
def get_datas_sub(request):
    print("开始计算")
    subdatas = request.param
    yield subdatas
    print("结束计算")

@pytest.fixture(scope="module",params=mul_datas,ids=mul_ids)
def get_datas_mul(request):
    print("开始计算")
    muldatas = request.param
    yield muldatas
    print("结束计算")

@pytest.fixture(scope="module",params=div_datas,ids=div_ids)
def get_datas_div(request):
    print("开始计算")
    divdatas = request.param
    yield divdatas
    print("结束计算")

# if __name__ == '__main__':
#     print(add_datas)