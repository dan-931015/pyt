# Paso 1: Define una variable de cada tipo de primitivo
entero = 42
flotante = 3.14
cadena = "Hola, mundo!"
booleano = True
nulo = None

# Paso 1.1: Concatena las otras variables a una cadena y guarda el resultado en una variable
resultado_cadena = (cadena + " El valor del entero es: " + str(entero) + ", el valor del flotante es: " + str(flotante) + ", el valor del booleano es: " + str(booleano) + " y el valor nulo es: " + str(nulo))

# Paso 1.2: Investigar sobre los límites de los enteros y los flotantes en Python

# Límites de enteros en Python
# En una plataforma de 64 bits, los enteros tienen un rango típico de -9,223,372,036,854,775,808 a 9,223,372,036,854,775,807.

# Límites de flotantes en Python
# Los flotantes en Python siguen el estándar IEEE 754 de precisión doble de 64 bits.
# El rango de valores flotantes permitidos es aproximadamente de ±1.797693e+308 a ±2.225074e-308.
# Python también tiene constantes especiales como `float('inf')` para infinito positivo y `float('-inf')` para infinito negativo.

# Paso 1.3: Aplicar la fórmula de la suma de los primeros n números pares y almacenar el resultado en una variable
# La fórmula para calcular la suma de los primeros n números pares es: suma = n * (n + 1) / 2

# Tomar el valor de n como un número entero
nu = 7
n= 14 // 2
# Calcular la suma de los primeros n números pares
suma = n * (n + 1) 

# Paso 2: Imprimir los resultados de las tareas anteriores
print("Entero:", entero)
print("Flotante:", flotante)
print("Cadena:", cadena)
print("Booleano:", booleano)
print("Nulo:", nulo)
print("Resultado de la concatenación:", resultado_cadena)
print("Suma de los primeros", nu, "números pares:", suma)