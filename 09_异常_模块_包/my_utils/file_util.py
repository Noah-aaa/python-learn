def print_flie_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        # for line in f:
        #     print(line) 读循环读文件中一行行的
        content = f.read()
        print(f"文件中的内容是{content}")  # 读文件中的所有内容
    except Exception as e:
        print(f"文件出现了异常：{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name,data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == "__main__":
   print_flie_info("D:/abc.txt")
   append_to_file("D:/abc.txt", "这只是测试语句")
   print_flie_info("D:/abc.txt")