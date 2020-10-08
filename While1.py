n=int(input("Ingrese un numero de casos: "))
m=1
while(m<=n):
    x=float(input("Ingrese el costo del pasaje sin tarjeta: "))
    y=float(input("Ingrese el costo del pasaje con tarjeta: "))
    a=float(input("Ingrese el costo de la tarjeta: "))
    b=float(input("Ingrese la carga inicial de la tarjeta: "))
    if(x<=y):
        print("No se recuperará")
    elif(a>b):
        c=0
        h=0
        r=x-y
        while(b>0):
            b=b-y
            h=h+r
            c=c+1
        if(h>=a):
            if(b!=0):
                c=c-1 
            c=c//2
            s=c//5
            d=c%5
            print(s," semanas ",d," días")
        else:
            print("no se recuperará")
        print("------------------------------------",h)
    m=m+1