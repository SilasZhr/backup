# coding: utf-8

import json
import web3,eth_abi
from web3 import Web3, HTTPProvider

u =  "xdai-archive.blockscout.com"

print(u, u.encode(encoding='UTF-8',errors='strict'))
w3 = Web3(Web3.HTTPProvider("https://"+u))
#new_block_filter = w3.eth.filter('latest')
with open('haus.abi', 'r') as f:
    abi = json.load(f)
g = open("haus_tx", "r")
address = "0xb0C5f3100A4d9d9532a4CfD68c55F1AE8da987Eb"
p = open("haus_holder_another", "w")
for i in g.readlines():
            test = w3.eth.contract(address = address, abi = abi)
            if True:
                    r = test.functions.balanceOf(i.strip()).call(block_identifier=16064581)
                    if int(r) > 0:
                        p.write(i)
                        print(i.strip(), r)
g.close()
p.close()
