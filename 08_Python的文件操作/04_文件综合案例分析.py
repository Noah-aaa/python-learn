f = open("D:/bill.txt", "w",encoding="UTF-8")

f.write("name,date,money,type,remarks\n周杰伦，2022-01-01，消费，正式\n")
f.write("周杰伦，2022-01-02，收入，正式\n")
f.write("周杰伦，2022-01-02，消费，测试\n")
f.write("林俊杰，2022-01-02，收入，正式\n")
f.write("林俊杰，2022-01-02，收入，正式\n")
f.write("林俊杰，2022-01-02，收入，测试\n")
f.write("张学友，2022-01-02，收入，正式\n")
f.write("张学友，2022-01-02，收入，测试\n")

f.close()
f = open("D:/bill.txt", "r", encoding="UTF-8")
g = open("D:/bill.txt.bak", "w", encoding="UTF-8")

for line in f:
        for i in line.strip().split('，'):
                if(i== "测试" ):
                        g.write(line)
f.close()
g.close()

g = open("D:/bill.txt.bak", "r", encoding="UTF-8")
print(g.read())