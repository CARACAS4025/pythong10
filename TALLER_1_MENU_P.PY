import random

def ejercicio_if_else():
    while True:
        print("\n--- Ejercicios IF-ELSE ---")
        print("1. Verificar si una letra es de las primeras o últimas del alfabeto.")
        print("2. Determinar en qué cuadrante está un ángulo.")
        print("3. Clasificar rendimiento de un estudiante.")
        print("4. Clasificar temperatura.")
        print("5. Verificar palabra 'Jengibre'.")
        print("6. Volver al menú principal.")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            letra = input("Introduce una letra: ").lower()
            if 'a' <= letra <= 'm':
                print("Es de las primeras letras del alfabeto.")
            elif 'n' <= letra <= 'z':
                print("Es de las últimas letras del alfabeto.")
            else:
                print("Entrada no válida. Introduce una letra.")
        
        elif opcion == '2':
            angulo = float(input("Introduce un ángulo en grados: "))
            if 0 <= angulo < 90:
                print("Primer cuadrante.")
            elif 90 <= angulo < 180:
                print("Segundo cuadrante.")
            elif 180 <= angulo < 270:
                print("Tercer cuadrante.")
            elif 270 <= angulo < 360:
                print("Cuarto cuadrante.")
            else:
                print("Ángulo fuera de rango.")
        
        elif opcion == '3':
            calificacion = float(input("Introduce la calificación: "))
            if calificacion > 4.5:
                print("Excelente")
            elif 3.5 < calificacion <= 4.5:
                print("Bueno")
            elif 3 <= calificacion <= 3.5:
                print("Regular")
            else:
                print("Insuficiente")
        
        elif opcion == '4':
            temperatura = float(input("Introduce la temperatura: "))
            if temperatura < 15:
                print("Frío")
            elif 15 <= temperatura <= 25:
                print("Templado")
            else:
                print("Cálido")
        
        elif opcion == '5':
            palabra = input("Escribe 'Jengibre': ").lower()
            if palabra == 'jengibre':
                print("No, ¡quiero un gran Jengibre!")
            else:
                print(f"¡Jengibre! No {palabra}")
        
        elif opcion == '6':
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

def ejercicio_while():
    while True:
        print("\n--- Ejercicios WHILE ---")
        print("1. Imprimir números del 20 al 1.")
        print("2. Imprimir números de 2 en 2 hasta el 50.")
        print("3. Contar vocales en una cadena.")
        print("4. Tirar un dado hasta obtener un 6.")
        print("5. Sumar dígitos de un número.")
        print("6. Volver al menú principal.")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            for i in range(20, 0, -1):
                print(i, end=" ")
            print()
        
        elif opcion == '2':
            for i in range(2, 51, 2):
                print(i, end=" ")
            print()
        
        elif opcion == '3':
            cadena = input("Introduce una cadena: ").lower()
            vocales = "aeiou"
            cuenta = sum(1 for char in cadena if char in vocales)
            print(f"Hay {cuenta} vocales en la cadena.")
        
        elif opcion == '4':
            dado = 0
            while dado != 6:
                dado = random.randint(1, 6)
                print(f"Tiraste un {dado}")
        
        elif opcion == '5':
            numero = input("Introduce un número: ")
            suma = sum(int(digito) for digito in numero if digito.isdigit())
            print(f"La suma de los dígitos es: {suma}")
        
        elif opcion == '6':
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

def ejercicio_for():
    while True:
        print("\n--- Ejercicios FOR ---")
        print("1. Sumar los cubos del 1 al 50.")
        print("2. Crear una pirámide de asteriscos.")
        print("3. Simular un tablero de ajedrez.")
        print("4. Invertir una cadena.")
        print("5. Buscar un elemento en una lista.")
        print("6. Volver al menú principal.")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            suma = sum(i**3 for i in range(1, 51))
            print(f"La suma de los cubos es: {suma}")
        
        elif opcion == '2':
            filas = int(input("Introduce el número de filas para la pirámide: "))
            for i in range(1, filas + 1):
                print(' ' * (filas - i) + '*' * (2 * i - 1))
        
        elif opcion == '3':
            tablero = ""
            for i in range(8):
                for j in range(8):
                    tablero += "B " if (i + j) % 2 == 0 else "N "
                tablero += "\n"
            print(tablero)
        
        elif opcion == '4':
            cadena = input("Introduce una cadena: ")
            print(f"Cadena invertida: {cadena[::-1]}")
        
        elif opcion == '5':
            lista = ['carro', 'moto', 'bicicleta', 'avión']
            elemento = input("Introduce un elemento a buscar: ")
            if elemento in lista:
                print(f"{elemento} está en la lista.")
            else:
                print(f"{elemento} no está en la lista.")
        
        elif opcion == '6':
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

def ejercicio_lambda():
    while True:
        print("\n--- Ejercicios LAMBDA ---")
        print("1. Sumar dos números.")
        print("2. Verificar si un número es par.")
        print("3. Ordenar una lista de tuplas.")
        print("4. Filtrar números mayores a 10.")
        print("5. Elevar al cuadrado una lista de números.")
        print("6. Volver al menú principal.")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            suma = lambda a, b: a + b
            a = int(input("Introduce el primer número: "))
            b = int(input("Introduce el segundo número: "))
            print(f"La suma es: {suma(a, b)}")
        
        elif opcion == '2':
            es_par = lambda x: x % 2 == 0
            numero = int(input("Introduce un número: "))
            print(f"¿Es par?: {es_par(numero)}")
        
        elif opcion == '3':
            tuplas = [(1, 'a'), (3, 'b'), (2, 'c')]
            tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
            print(f"Tuplas ordenadas: {tuplas_ordenadas}")
        
        elif opcion == '4':
            numeros = [int(n) for n in input("Introduce una lista de números separados por espacio: ").split()]
            mayores_10 = list(filter(lambda x: x > 10, numeros))
            print(f"Números mayores a 10: {mayores_10}")
        
        elif opcion == '5':
            numeros = [int(n) for n in input("Introduce una lista de números separados por espacio: ").split()]
            cuadrados = list(map(lambda x: x**2, numeros))
            print(f"Cuadrados: {cuadrados}")
        
        elif opcion == '6':
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ejercicios IF-ELSE")
        print("2. Ejercicios WHILE")
        print("3. Ejercicios FOR")
        print("4. Ejercicios LAMBDA")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            ejercicio_if_else()
        elif opcion == '2':
            ejercicio_while()
        elif opcion == '3':
            ejercicio_for()
        elif opcion == '4':
            ejercicio_lambda()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
