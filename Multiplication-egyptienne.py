a = int(input("type a number : "))
b = int(input("type another number : "))
x = a
y = b
z = 0

while x != 0 :
    if (x % 2) == 1 :
        z = z + y 
    y = y + y
    x = int(x/2)
print(z)
##commentaire