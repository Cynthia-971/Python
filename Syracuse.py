def collatz(a):
    nb=0
    while a!=1 :
        if a%2==0 :
            a = a//2
        else :
            a = a*3+1
        print(a)
        nb+=1
    return (nb)
var = collatz(int(input()))
print(var)