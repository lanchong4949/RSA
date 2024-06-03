"""
    Dp & Dq泄露攻击
    Dp=dmod(p-1)
    Dq=dmod(q-1)
    没有e，有p,q,Dp,Dq
"""
import Crypto.Util.number
import gmpy2
p=
q=
Dp=
Dq=
c=
invp=gmpy2.invert(p,q)
m1=gmpy2.powmod(c,Dp,p)
m2=gmpy2.powmod(c,Dq,q)
m=(((m2-m1)*invp)%q)*p+m1
print(Crypto.Util.number.long_to_bytes(m))