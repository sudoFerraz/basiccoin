import json, hashlib
#These deterministic functions are used a lot in blockchain.py and consensus.py
def package(dic):return json.dumps(dic)
def unpackage(dic):return json.loads(dic)
def det_hash(x):
    x=unpackage(package(x))
    def det_list(l):
        out=''
        for i in sorted(l):
            out+=det(i)+','
        return '['+out+']'
    def det_dic(dic):
        out=''
        for i in sorted(dic.keys()):
            out+=det(i)+':'+det(dic[i])+','
        return '{'+out+'}'
    def det(x):return {list:det_list, dict:det_dic}.get(type(x), str)(x)
    def sha256(x):return hashlib.sha256(x).hexdigest()
    return sha256(det(x))

