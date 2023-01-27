"""
和文件相关的类
"""
import json

from data_define import *
# 先定义一个抽象类来用作顶层设计，确定那些功能要实现


class FileReader:

    def read_data(self) -> list[Record]:
        """读取文件的数据。读到的每一条数据都转换为Record对象。将他们封装成list返回"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    # 实现父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)  # 将json数据构建成python字典
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)
        f.close()
        return record_list


if __name__ == "__main__":
    text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
