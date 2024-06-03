"""
    Rabin攻击

    Rabin攻击是一种针对RSA算法中模数p和q的共模攻击
    利用模数p和q的共模性，通过分解p和q的乘积n，得到私钥d，从而实现对RSA算法的解密。
    有p，q没有e
"""
import Crypto.Util.number
import gmpy2
p=
q=
c=
n=p*q
c1=gmpy2.powmod(c,(p+1)//4,p)
c2=gmpy2.powmod(c,(q+1)//4,q)
cp1=p-c1
cp2=q-c2
t1=gmpy2.invert(p,q)
t2=gmpy2.invert(q,p)
m1=(q*c1*c2+p*c2*t1)%n
m2=(q*c1*t2+p*cp2*t1)%n
m3=(q*cp1*t2+p*c2*t1)%n
m4=(q*cp1*t2+p*cp2*t1)%n
print(Crypto.Util.number.long_to_bytes(m1))
print(Crypto.Util.number.long_to_bytes(m2))
print(Crypto.Util.number.long_to_bytes(m3))
print(Crypto.Util.number.long_to_bytes(m4))