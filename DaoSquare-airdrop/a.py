import os
import csv

path = "/root/DaoSquare-airdrop/" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
f = open("haus_addr", "w")
addr_list = []
for file in files: #遍历文件夹
     #print(file)
     if file.startswith("transa"):
        print(file)
        csvFile = open(path+file, "r")
        reader = csv.reader(csvFile)
        for item in reader:
                # 忽略第一行
                if reader.line_num == 1:
                    continue
                if len(item) < 4:
                    continue
                else:
                    addr_list.append(item[3])
                    addr_list.append(item[4])
        csvFile.close()
addr_list = list(set(addr_list))
print(addr_list, len(addr_list))
with open("haus_tx", 'w') as g:
    for i in addr_list:
        g.write(i+"\n")
g.close()

