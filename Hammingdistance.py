
def hammingDistance(x, y):
    xor = x ^ y
    dist = 0
    print('1-',xor)
    while xor:
        dist += 1
        print('dist-',dist)
        print('2--',xor&(xor-1))
        xor &= xor - 1
        print('2-',xor)
    return dist

x = 1
y = 4
print(hammingDistance(x, y))
