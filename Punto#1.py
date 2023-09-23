n1 = int(input("ingrese el primer número"))
n2 = int(input("ingrese el segundo número"))
n3 = int(input("ingree el tercer número"))
if n1 and n1 > n3:
    print("El número mayor es: ",n1) 
elif n2 > n1 and n2 > n3:
    print("El número mayor es:",n2)
elif n3 > n1 and n3 > n2:
    print("El número mayor es: ",n3)
else:
    print("No se pudo establecer el mayor") 