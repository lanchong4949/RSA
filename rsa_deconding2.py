'''
    共享素数
    同时生成多个公钥，生成公钥中有两组N使用了相同的素数
    两组N不互素
    两组公钥及密文
'''
import Crypto.Util.number
import gmpy2
e=
n1=
n2=
c1=
c2=
p=gmpy2.gcd(n1,n2)
q=n1//p
d=gmpy2.invert(e,(p-1)*(q-1))
print(Crypto.Util.number.long_to_bytes(gmpy2.powmod(c1,d,n1)))
