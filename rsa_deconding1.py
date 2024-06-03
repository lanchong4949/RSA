"""
    因数分解
    N比较小，尝试直接分解N获得P，q，从而获得私钥
    N看起来比较小
"""
import gmpy2
import Crypto.Util.number
p = 305
q = 5
c = 61
e = 65537
d = gmpy2.invert(e, (p - 1) * (q - 1))
m = gmpy2.powmod(c, d, p * q)
print(Crypto.Util.number.long_to_bytes(m))
