# 使用Union类型必须要导包
from typing import Union

#
my_list: list[Union[int, str]] = [1, 2, "3333"]


def func(data: Union[list,str]) -> Union[str, int]:
    pass

