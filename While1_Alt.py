n=int(input("Ingrese un numero de casos: "))
for i in range(n):
    x=float(input("Ingrese el costo del pasaje sin tarjeta: "))   
    y=float(input("Ingrese el costo del pasaje con tarjeta: "))
    a=float(input("Ingrese el costo de la tarjeta: "))    
    b=float(input("Ingrese la carga inicial de la tarjeta: "))
    cu=0
    cs=0
    sw=1
    gasto=x
    if(x<=y):
        sw=0
        print("No se recupera")
    else:
        while(gasto<=a):
            if(b-y>0):
                b=b-y
            else:
                a=a+(b-y)
            cu=cu+1
            gasto=gasto+x
    if(sw==1):
        cd=cu//2
        if(cd>=5):
            cs=cd//5
            cd=cd%5    
        print(cs,"semanas",cd,"dias")