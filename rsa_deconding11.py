"""
    Schemidt Samoa 攻击
    p,q,n，n和其欧拉值的逆元不存在
"""
import Crypto.Util.number
import gmpy2
p=
q=
c=
phi=(p-1)*(q-1)
d=gmpy2.invert(p*q,phi)
print(Crypto.Util.number.long_to_bytes(gmpy2.powmod(c,d,p*q)))