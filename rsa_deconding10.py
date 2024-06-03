"""
    Dp泄露攻击
    除了公钥还有Dp，e也比较小
"""
import Crypto.Util.number
import gmpy2
Dp=
e=
n=
c=
for x in range(1,e):
    if (e*Dp-1)%x==0:
        p=(e*Dp-1)//x+1
        if n%p==0:
            q=n//p
            d=gmpy2.invert(e,(p-1)*(q-1))
            m=gmpy2.powmod(c,d,n)
            print(Crypto.Util.number.long_to_bytes(m))