n=int(input("Ingrese un numero: "))
c=1
h=1
while(c<=n):
    f=0
    for i in range(c):
        f=(f+h)
    h=f
    c=c+1
print("El factorial de ",n," es: ",f)
