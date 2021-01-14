import pytest


class Test_Cala:

    @pytest.mark.second
    def test_sub(self, get_calc, get_datas_sub):  # 调用conftest文件的get_add_data和get_cal方法
        sub = None
        try:
            sub = get_calc.sub(get_datas_sub[0], get_datas_sub[1])
            print(f'a-b:{get_datas_sub[0]} - {get_datas_sub[1]}={get_datas_sub[0] - get_datas_sub[1]}')
            if isinstance(sub, float):
                sub = round(sub, 2)
        except Exception as r:
            print(r)
        pytest.assume(sub == get_datas_sub[2])


    @pytest.mark.first
    def test_add(self,get_calc,get_datas_add):# 调用conftest文件的get_add_data和get_cal方法
        add = None
        try:
            add = get_calc.add(get_datas_add[0],get_datas_add[1])
            print(f'a+b:{get_datas_add[0]}+{get_datas_add[1]}={get_datas_add[0]+get_datas_add[1]}')
            if isinstance(add,float):
                add = round(add,2)
        except Exception as r :
            print(r)
        pytest.assume(add == get_datas_add[2])


    @pytest.mark.third
    def test_mul(self,get_calc,get_datas_mul):
        mul = None
        try:
            mul = get_calc.mul(get_datas_mul[0],get_datas_mul[1])
            print(f'a*b:{get_datas_mul[0]}*{get_datas_mul[1]}={get_datas_mul[0]*get_datas_mul[1]}')
            if isinstance(mul,float):
                mul = round(mul,2)
        except Exception as q:
            print(q)
        pytest.assuem(mul == get_datas_mul[2])


    @pytest.mark.fourth
    def test_div(self,get_calc,get_datas_div):
        div = None
        try:
            div = get_calc.div(get_datas_div[0],get_datas_div[1])
            print(f'a/b:{get_datas_div[0]} / {get_datas_div[1]}={get_datas_div[0] / get_datas_div[1]}')
            print(div)
            if isinstance(div,float):
                div = round(2)
        except Exception as w:
            print(w)
        pytest.assuem(div == get_datas_div[2])
#     '''
#
if __name__ == '__main__':
    pytest.main(['test_calc_new.py','-sq'])