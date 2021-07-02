import os
import csv


address = []

def get_gitcoin():
    path = "/root/DaoSquare-airdrop/gitcoin-eth.csv" 
    csvFile = open(path, "r")
    reader = csv.reader(csvFile)
    test = []
    global address
    for item in reader:
                # 忽略第一行
                if reader.line_num == 1:
                    continue
                if len(item) < 6:
                    continue
                else:
                    tx_from = item[3]
                    tx_to = item[4]
                    if tx_to == "0x9ac9c636404c8d46d9eb966d7179983ba5a3941a" and tx_from != "0x9ac9c636404c8d46d9eb966d7179983ba5a3941a":
                        test.append(tx_from)
    csvFile.close()
    address = address + test
    print(path, len(test) )

def get_ant():
    path = "/root/DaoSquare-airdrop/ant.csv" 
    csvFile = open(path, "r")
    reader = csv.reader(csvFile)
    test = []
    global address
    for item in reader:
                # 忽略第一行
                if reader.line_num == 1:
                    continue
                if len(item) < 1:
                    continue
                else:
                    test.append(item[0])
    csvFile.close()
    address = address + test
    print(path, len(test) )

def get_anc():
    path = "/root/DaoSquare-airdrop/anc.csv" 
    csvFile = open(path, "r")
    reader = csv.reader(csvFile)
    test = []
    global address
    for item in reader:
                # 忽略第一行
                if reader.line_num == 1:
                    continue
                if len(item) < 1:
                    continue
                else:
                    test.append(item[0])
    csvFile.close()
    address = address + test
    print(path, len(test) )

def get_haus_mainnet():
    path = "/root/DaoSquare-airdrop/haus_mainnet.csv" 
    csvFile = open(path, "r")
    reader = csv.reader(csvFile)
    test = []
    global address
    for item in reader:
                # 忽略第一行
                if reader.line_num == 1:
                    continue
                if len(item) < 1:
                    continue
                else:
                   test.append(item[0])
    csvFile.close()
    address = address + test
    print(path, len(test) )

def get_thedao():
    path = "/root/DaoSquare-airdrop/TheDAO.csv" 
    csvFile = open(path, "r")
    reader = csv.reader(csvFile)
    test = []
    global address
    for item in reader:
                # 忽略第一行
                if reader.line_num == 1:
                    continue
                if len(item) < 6:
                    continue
                else:
                    tx_from = item[4]
                    tx_to = item[5]
                    if tx_from not in test:
                        test.append(tx_from)
                    if tx_to not in test:
                        test.append(tx_to)
                    if len(test) == 1000:
                        break
    address = address + test
    csvFile.close()
    print(path, len(test) )

def get_haus_member():
    path = "/root/DaoSquare-airdrop/haus_member.csv" 
    csvFile = open(path, "r")
    reader = csv.reader(csvFile)
    test = []
    global address
    for item in reader:
                # 忽略第一行
                if reader.line_num == 1:
                    continue
                if len(item) < 1:
                    continue
                else:
                    test.append(item[0])
    csvFile.close()
    address = address + test
    print(path, len(test) )

def get_haus_holder():
    path = "/root/DaoSquare-airdrop/haus_holder" 
    f = open(path, "r")
    test = []
    global address
    for item in f.readlines():
                test.append(item.strip())
    f.close()
    address = address + test
    print(path, len(test) )

def get_haus_1x():
    path = "/root/DaoSquare-airdrop/haus_holder_1x" 
    f = open(path, "r")
    test = []
    global address
    for item in f.readlines():
                test.append(item.strip())
    f.close()
    address = address + test
    print(path, len(test) )


def get_haus_2x():
    path = "/root/DaoSquare-airdrop/haus_holder_2x" 
    f = open(path, "r")
    test = []
    global address
    for item in f.readlines():
                test.append(item.strip())
    f.close()
    address = address + test
    print(path, len(test) )

def get_gitcoin_zk():
    path = "/root/DaoSquare-airdrop/gr9-zk" 
    f = open(path, "r")
    test = []
    global address
    for item in f.readlines():
                test.append(item.strip())
    f.close()
    address = address + test
    print(path, len(test) )

if __name__ == '__main__':
    get_anc()
    get_ant()
    get_gitcoin()
    get_haus_holder()
    get_haus_1x()
    get_haus_2x()
    get_haus_mainnet()
    get_haus_member()
    get_thedao()
    get_gitcoin_zk()
    print("total address:", len(address))
    address = list(set(address))
    print("total address:", len(address))
    f = open("cco_list", "w")
    for i in address:
        if len(i) > 10:
            f.write(i+"\n")
    f.close()





#get_thedao()
#addr_list = list(set(addr_list))


