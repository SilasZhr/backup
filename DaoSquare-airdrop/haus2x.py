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
address = "0x04a52DDE2D307C33Fd1Ad104145872b8f46340E5"
p = open("haus_holder_2x", "w")
for i in g.readlines():
            test = w3.eth.contract(address = address, abi = abi)
            if True:
                    r = test.functions.balanceOf(i.strip()).call(block_identifier=16064581)
                    if int(r) > 0:
                        p.write(i)
                        print(i.strip(), r)
g.close()
p.close()
