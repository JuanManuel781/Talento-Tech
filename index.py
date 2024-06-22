print("Hola mundo ")

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (1, 2, 3, 2, 4, 5)

print('esta es una lista: ',mi_lista)
print('esta es una tupla:',mi_tupla)

Primer_numero = input("Ingrese un numero: ")
Segundo_numero = input("Ingrese un numero: ")
resultado = print('resultado es:', (int(Primer_numero) * int(Segundo_numero)))

print("Hola mundo desde la nueva rama denominada prueba ")

edad = input("Ingrese un numero: ")

if int(edad) >= 18: 
    print('mayor de edad')
else:
    print('menor de edad')

for lista in mi_lista:
    print(lista)