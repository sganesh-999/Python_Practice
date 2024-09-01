def bin(x):
    binary=""
    while (x > 0):
        binary+=str(x%2)
        x=x//2
    return binary[::-1]

n=5 
o=[]
for i in range(5):
    o.append(bin(i).count('1'))
print(o)
