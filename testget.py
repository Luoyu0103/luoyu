import pytest

# class Test_Demo():
    # def test_demo(self):
    #     a=5
    #     b=-1
    #     assert a!=b
    #     print('我的第一个测试用例')

# def add_function(a,b):
#     return a+b
# @pytest.mark.parametrize("a,b,expected",[(3,5,8),(-1,-2,-3),(100,200,300)],ids=["int","minus","bigint"])


# def test_add(a,b,expected):
#     assert add_function(a,b) == expected

# @pytest.mark.parametrize("a",[0,1])
# @pytest.mark.parametrize("b",[2,3])
# def test_foo(a,b):
#     print("测试数据组合:a->%s,b->%s" % (a,b))

# def setup_module():
#     print(
#         "\nsetup_module:整个test_module.py模块只执行一次"
#     )
# def teardown_module():
#     print(
#         "\nteardown_module:整个test_module.py模块只执行一次"
#     )

def setup_function():
    print("\nsetup_function:每个不在类中的用例开始前都会执行")
def teardown_function():
    print("\nteardown_function:每个不在类中的用例结束后都会执行")
def test_one():
    print("正在执行测试模块---------test_one")
def test_two():
    print("正在执行测试模块---------test_two")

