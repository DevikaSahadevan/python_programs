n1 = 0
n2 = 1
num = int(input("enter limit"))
print(n1)
print(n2)
for i in range(0, num - 2):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3

