import yaml
import pytest,sys,os
sys.path.append(os.getcwd())
from base.get_data import GetData

def read_sum():
    # 定义一个空列表
    result = []
    # 读取文件
    yaml_data=GetData.get_yaml_data("sum.yaml")
    for i in yaml_data.values():
        result.append(tuple(i.values()))
    return result


class TestSum:
    @pytest.mark.parametrize("a,b,c", read_sum())
    def test_01(self, a, b, c):
        assert a + b == c
