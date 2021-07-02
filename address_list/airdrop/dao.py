import requests
from easygraphql import GraphQL


url_xdai = "https://api.thegraph.com/subgraphs/name/odyssy-automaton/daohaus-xdai"
url_mainnet = "https://api.thegraph.com/subgraphs/name/odyssy-automaton/daohaus"
url_idchain = "https://graph.idchain.one/subgraphs/name/idchain/daohaus-supergraph"
query = '''
query membersList($contractAddr: String!, $skip: Int) {
  daoMembers: members(
    where: {molochAddress: $contractAddr}
    orderBy: shares
    orderDirection: desc
    first: 1000
    skip: $skip
  ) {
    id
    delegateKey
    shares
    loot
    kicked
    jailed
    tokenTribute
    didRagequit
    memberAddress
    exists
    createdAt
    }
}
'''


def get_name(address):
    url = "https://data.daohaus.club/dao/"
    res = requests.get(url+address)
    return res.json()[0]['name']

def get_DAO_list():
    with open("DAO_list", "r") as f :
        for line in f.readlines():
            para = line.split('/')
            #print(para)
            if para[-2] == '0x64':
                u = url_xdai
            elif para[-2] == '0x1':
                u = url_mainnet
            elif para[-2] == '0x4a':
                u = url_idchain
            get_member(u, para[-1].strip())
            

def get_member(url, address):
    graphql = GraphQL(url)
    variables = {
        "contractAddr": "0xee629a192374caf2a72cf1695c485c5c89611ef2",
        "skip": 0
    }
    #print(url, address)
    variables['contractAddr'] = address
    data, errors = graphql.execute(query, variables)
    name = get_name(address)
    a = []
    #print(data)
    with open(name+".csv", 'w') as f:
        for member in data['daoMembers']:
            if member['exists'] == True and  (int(member['shares']) > 0  or  int(member['loot']) > 0):
                a.append(member['memberAddress'])
        a = list(set(a))
        f.write(name+"\t"+str(len(a))+"\n")
        for i in a:
            f.write(i+'\n')

    print(name, len(a))


if __name__ == '__main__':

    get_DAO_list()


