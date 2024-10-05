#1. Determinar si una lista es un palíndromo
#-------------------------------------------
def palindromo(L):
    return L == L[::-1] #slice para invertir la lista [::-1]


# Pedimos al usuario que introduzca los elementos de la lista
entrada = input("Introduce los elementos de la lista separados por comas: ")
lista = entrada.split(',')

# Quitamos posibles espacios en blanco alrededor de cada elemento
lista = [elem.strip() for elem in lista]

# Verificamos si la lista es un palíndromo
if palindromo(lista):
    print("True")
else:
    print("False")

#2. Encontrar el elemento máximo en una lista
#---------------------------------------------
def maximo(lista):
    max_valor = lista[0]  # Inicializamos el máximo con el primer elemento de la lista
    
    for elemento in lista[1:]:  # Iteramos sobre los elementos desde el segundo en adelante
                                #slice [1:] desde el elemento indice 1 hasta el final
        if elemento > max_valor:
            max_valor = elemento  # Actualizamos el máximo si encontramos uno mayor
    
    return max_valor  # Devolvemos el valor máximo encontrado

# Pedimos al usuario que introduzca los elementos de la lista separados por comas
entrada = input("Introduce los números de la lista separados por comas: ")
lista = [int(x.strip()) for x in entrada.split(',')]  # Convertimos los valores en enteros

# Llamamos a la función maximo y mostramos el resultado
resultado = maximo(lista)
print(f"El valor máximo de la lista es: {resultado}")


#3. Contar los elementos en una lista
#---------------------------------------
def longitud(lista):
    contador = 0  # Inicializamos el contador
    for elemento in lista:  # Iteramos sobre cada elemento de la lista
        contador += 1  # Incrementamos el contador en cada iteración
    return contador  # Devolvemos el valor del contador

# Pedimos al usuario que introduzca los elementos de la lista separados por comas
entrada_lista = input("Introduce los elementos de la lista separados por comas: ")
lista = [x.strip() for x in entrada_lista.split(',')]  # Creamos la lista eliminando espacios
entrada_longitud = int(input("Introduce la longitud de la lista: "))

# Llamamos a la función longitud y mostramos el resultado
resultado = longitud(lista)
print(f"La longitud de la lista es: {resultado}")
if resultado == entrada_longitud: 
    print("True")
else:
    print("False")

#4. Generar la sucesión de Fibonacci 
#------------------------------------
def fibonacci(n):
    # Caso base: F(0) = 0 y F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pedimos al usuario que introduzca el valor de N
n = int(input("Introduce el valor de N: "))

# Llamamos a la función fibonacci y mostramos el resultado
resultado = fibonacci(n)
print(f"El {n}-ésimo número de la sucesión de Fibonacci es: {resultado}")
