n = int(input("type a number : "))
m = int(input("type another number : "))

i = m
z = 1
list = []
list2 = []
j = 0
a = n*m

##multiplication entre n et m
print(a)

##liste des nombres inférieurs à n et m
while n >= z :
    list.append(z)
    list2.append(i)
    print("%(z)d| %(i)d" %{"z":z,"i":i})
    z=2
    i = m*z

list = list[::-1]
list2 = list2[::-1]

list1=[]


##opération permettant de trouver les nombres dont la somme est égale à nm
for num in list2:
    while num<=a:
        a = a - num
        list1.append(num)

count = 0

s = " + ".join([str(l) for l in list1])
print("l'addition ",s, "=", n*m)