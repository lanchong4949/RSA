"""
    低加密指数攻击（小明文攻击）
    公钥中的e获得明文m足够小
    加密得到的值c（密文）小于N
    e很小
"""
import gmpy2
import Crypto.Util.number
e=
c=
print(Crypto.Util.number.long_to_bytes(gmpy2.iroot(c,e)[0]))