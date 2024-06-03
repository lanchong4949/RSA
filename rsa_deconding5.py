"""
    共模攻击
    两组公钥使用相同的模数N、不同的私钥，同时对同一组明文进行加密
    必须加密同一组明文而且只能求出该密文的明文
    两组公钥使用的e是互素的
    两组公钥和密文，但是n是相同的，e1和e2互素
"""
import Crypto.Util.number
import gmpy2
e1=
e2=
n=
c1=
c2=
s=gmpy2.gcdext(e1,e2)
s1=s[1]
s2=s[2]
print(Crypto.Util.number.long_to_bytes(gmpy2.powmod(c1,s1,n)*gmpy2.powmod(c2,s2,n)%n))