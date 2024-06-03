"""
    p-1光滑攻击
    光滑数：可分解为小素数乘积的正整数
"""
import gmpy2
a=2
n=2
N=
while True:
    a=gmpy2.powmod(a,n,N)
    res=gmpy2.gcd(a-1,N)
    if res!=1 and res!=N:
        q=N//res
        print(res,q,res*q==N)
        break
    n+=1
