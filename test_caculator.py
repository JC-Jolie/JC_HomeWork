# pytest实战练习1：
# 1、补全计算器（加减乘除）的测试用例
# 2、使用参数完成测试用例的自动生成
# 3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

import pytest

from exercise.caculator import Caculator


class TestCaculator:
    def setup_class(self):
        self.cal = Caculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, sum", [(1, 2, 3), (-1, -2, -3), (1000, 2000, 3000)],
                             ids=["add_minint", "add_minus", "add_bigint"])
    def test_add(self, a, b, sum):
        assert sum == self.cal.add(a, b)

    @pytest.mark.parametrize("a, b, sum", [(5, 3, 2), (-5, -3, -2), (5000, 2000, 3000)],
                             ids=["sub_minint", "sub_minus", "sub_bigint"])
    def test_sub(self, a, b, sum):
        assert sum == self.cal.sub(a, b)

    @pytest.mark.parametrize("a, b, sum", [(1, 2, 2), (-3, -4, 12), (1000, 2000, 2000000)],
                             ids=["mul_minint", "mul_minus", "mul_bigint"])
    def test_mul(self, a, b, sum):
        assert sum == self.cal.mul(a, b)

    @pytest.mark.parametrize("a, b, sum", [(4, 2, 2), (-4, -2, 2), (2000, 1000, 2)],
                             ids=["div_minint", "div_minus", "div_bigint"])
    def test_div(self, a, b, sum):
        assert sum == self.cal.div(a, b)
