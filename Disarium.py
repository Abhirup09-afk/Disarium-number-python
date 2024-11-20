import math

x = int(input("Enter a number: "))
y = len(str(x))

z = x
a = 0

while x != 0:
    for i in range(y, 0, -1):
        
        b = (x % 10)
        c = math.pow(b, i)
        
        a += c
        
        x //= 10

if z == a:
    print(f"{z} is an disarium number.")

else:
    print(f"{z} is not an disarium number")


