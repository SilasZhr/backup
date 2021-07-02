import requests
import datetime

url = "https://api.zksync.io/api/v0.1/account/0x9ac9c636404c8d46d9eb966d7179983ba5a3941a/history/"
f = open("gr9-zk", 'w')
wallet = "0x9ac9c636404c8d46d9eb966d7179983ba5a3941a"
for i in range(0,10000,100):
    u = url + str(i) + "/100"
    print(u)
    res = requests.get(u)
    if res.text == '[]':
        break
    else:
        tx_list = res.json()
        for tx in tx_list:
            if not 'from' in  tx['tx']:
                continue
            tx_from  = tx['tx']['from']
            tx_to = tx['tx']['to']
            tx_amount = tx['tx']['amount']
            tx_token = tx['tx']['token']
            tx_time = tx['created_at']
            if  datetime.datetime.strptime(tx_time, '%Y-%m-%dT%H:%M:%S.%fZ') < datetime.datetime.strptime('2021-03-08T02:43:16.620655Z', '%Y-%m-%dT%H:%M:%S.%fZ'):
                continue
            if tx_from != wallet and tx_to == wallet :
                print(tx_from)

                f.write(tx_from+"\n")

f.close()