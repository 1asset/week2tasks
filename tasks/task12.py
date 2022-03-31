n = int(input())

print ("____________________________________________")

a0 = 1

for i in range(1, n+1):
    a1 = (a0+1)/i
    print(a1)
    a0 = a1
