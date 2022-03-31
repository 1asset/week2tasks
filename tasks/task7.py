from math import factorial

x = float(input())
n = int(input())

total = x

for i in range (1, n+1):
    total += (2*i-1)*x/factorial((2*i)*(2*i+1))
    
print(total)
