import pytest
from original import rect_area,func

@pytest.fixture(params=[1, 2, 3])
def need_data(request): # 传入参数request 系统封装参数
    return request.param # 取列表中单个值，默认的取值方式
def test_tect_area(need_data):
    print("------->test_tect_area",need_data)
    assert rect_area(need_data) != 4 # 断言need_data不等于3
    # assert rect_area(need_data) != 3 # 断言need_data不等于3

def test_a(need_data):
    print("------->test_a")
    assert func(need_data) != 4 # 断言need_data不等于3
    # assert func(need_data) != 6 # 断言need_data不等于3

if __name__ == '__main__':
    pytest.main("-s test_ex.py")
