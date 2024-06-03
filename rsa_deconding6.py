"""
    低加密指数广播攻击
    使用多组公钥加密同一消息且公钥中加密指数e相同
    中国剩余定理
    e比较小，用同一个e，不同n
"""
import Crypto.Util.number
import gmpy2
e=
n_list=[]
c_list=[]
N=1
for n in n_list:
    N*=n
M_list=[]
for n in n_list:
    M_list.append(N//n)
t_list=[]
for i in range(len(n_list)):
    t_list.append(gmpy2.invert(M_list[i],n_list[i]))
summary=0
for i in range(len(n_list)):
    summary=(summary+c_list[i]*t_list[i]*M_list[i])%N
m=gmpy2.iroot(summary,e)[0]
print(Crypto.Util.number.long_to_bytes(m))