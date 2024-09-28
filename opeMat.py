import math

def calculadora():
    while True:
        try:
            num1 = float(input("Ingrese un numero: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Por favor, ingrese numeros validos.")
            continue

        print("\nSeleccione una operación:")
        print("1: Sumar")
        print("2: Restar")
        print("3: Multiplicar")
        print("4: Dividir")
        print("5: Potencia")
        print("6: Radicacion")
        print("7: Porcentaje")
        print("8: Todos")

        opcion = input("Ingrese el numero de la operacion deseada: ")

        if opcion == '1':
            print("La suma es:", num1 + num2)
        elif opcion == '2':
            print("La resta es:", num1 - num2)
        elif opcion == '3':
            print("La multiplicacion es:", num1 * num2)
        elif opcion == '4':
            if num2 == 0:
                print("ERROR: no se puede dividir entre 0")
            else:
                print("La division es:", num1 / num2)
                print("La division modular es:", num1 % num2)
        elif opcion == '5':
            if num1 == 0 and num2 <= 0:
                print("ERROR: 0 elevado a una potencia no positiva no esta definido")
            else:
                print("La potencia es:", num1 ** num2)
        elif opcion == '6':
            if num1 < 0 and num2 % 2 == 0:
                print("ERROR: no se puede calcular la raiz cuadrada de un número negativo")
            else:
                print("La radicación es:", round(num1 ** (1 / num2),2))
        elif opcion == '7':
            porcentaje = (num1 * num2) / 100
            print(f"El {num2}% de {num1} es:", porcentaje)
        elif opcion == '8':
            print("La suma es:", num1 + num2)
            print("La resta es:", num1 - num2)
            print("La multiplicacion es:", num1 * num2)
            if num2 == 0:
                print("ERROR: no se puede dividir entre 0")
            else:
                print("La division es:", num1 / num2)
                print("La division modular es:", num1 % num2)
            if num1 == 0 and num2 <= 0:
                print("ERROR: 0 elevado a una potencia no positiva no esta definido")
            else:
                print("La potencia es:", num1 ** num2)
            if num1 < 0 and num2 % 2 == 0:
                print("ERROR: no se puede calcular la raiz cuadrada de un numero negativo")
            else:
                print("La radicacion es:", round(num1 ** (1 / num2),2))
            porcentaje = (num1 * num2) / 100
            print(f"El {num2}% de {num1} es:", porcentaje)
        else:
            print("Opcion no valida.")

        continuar = input("¿Desea realizar otro calculo? (s/n): ").lower()
        if continuar != 's':
            break

calculadora()
