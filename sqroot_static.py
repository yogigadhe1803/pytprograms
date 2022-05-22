class Myclass:
    @staticmethod
    def sroot(x):
        res = x ** 0.5
        return res

res = Myclass.sroot(16)

print('Square root of 16 is = ',res)