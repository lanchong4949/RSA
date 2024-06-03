"""
    Wiener攻击（连分数攻击）（低解密指数攻击）
    使用连分数分解的方式在d较小时获得私钥d
    n和e比较接近
"""
import Crypto.Util.number
import gmpy2


class ContinuedFractionAttack:
    def __init__(self, numerator, denumerator):
        self.numberlist = []
        self.fractionlist = []
        self.GenerateNumberList(numerator, denumerator)
        self.GenerateFractionList()

    def GenerateNumberList(self, numerator, denumerator):
        while numerator != 1:
            quotient = numerator // denumerator
            remainder = numerator % denumerator
            self.numberlist.append(quotient)
            denumerator = remainder

    def GenerateFractionList(self):
        self.fractionlist.append([self.numberlist[0], 1])
        for i in range(1, len(self.numberlist)):
            numerater = self.numberlist[i]
            denumerator = 1
            for j in range(i):
                temp = numerater
                numerater = denumerator + numerater * self.numberlist[i - j - 1]
                denumerator = temp

            self.fractionlist.append([numerater, denumerator])


n = 16449445646545645645645576876786786786769846598651398654653465148653264546532
e = 6464689848949848678645645654687676767886986598654865465486514865486548656584656586584654865
c = 1566849849849796786786786786786786867689698658659865986589658659865986598658959869865856865574745965896541653
a = ContinuedFractionAttack(e, n)
for k, d in a.fractionlist:
    s = Crypto.Util.number.long_to_bytes(gmpy2.powmod(c, d, n))
    try:
        print(s.decode())
    except Exception:
        pass
