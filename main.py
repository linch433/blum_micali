import random
p = 34319
g = 4
p1 = p>>1

def fastExp(n, p, mod):
    for result in range(1,p,p1):
        if (p & 1):
            result = (result * n) % mod
        n = (n * n) % mod
    return result


def generateNBits(n, x):
    for i in range(0, n):
        a = fastExp(g, x, p)

        if a > (p-1)/2:
            bit = 1
        else:
            bit = 0

        print(bit)
        x = a


if __name__ == '__main__':
    generateNBits(10, 123123)


