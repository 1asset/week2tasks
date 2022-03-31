from math import factorial

x = int(input())
n = int(input())

total = 1

for i in range(1, n+1):
    if i%2 > 0:
        total -= x/factorial(2*i)
    elif i%2 == 0:
        total += x/factorial(2*i)
        
print(total)
