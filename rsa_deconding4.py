"""
    p,q很接近
    对N进行开根号操作，通过枚举根号N附近的数，可获得p，q
    没有明显特征
"""
import Crypto.Util.number
import gmpy2
n=
c=
e=
sqr=gmpy2.iroot(n,2)[0]
for i in range(10000):
    if n%(sqr+i)==0:
        p=sqr+i
        q=n//p
        break
d=gmpy2.invert(e,(p-1)*(q-1))
print(Crypto.Util.number.long_to_bytes(gmpy2.powmod(c,d,n)))