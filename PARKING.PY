import datetime

# Constantes
TOTAL_VEHICULOS = 50
TOTAL_MOTOS = 25
TARIFA_HORA = 2000  # Tarifa por hora
DESCUENTO = 0.15  # Descuento del 15%
HORA_INICIO = 6  # 6 AM
HORA_FIN = 22  # 10 PM
DURACION_JORNADA = HORA_FIN - HORA_INICIO

# Inicialización de parqueadero
def inicializar_parqueadero():
    parqueadero = [['v' + str(i + 1) for i in range(TOTAL_VEHICULOS // 10)] for _ in range(5)]
    parqueadero.append(['m' + str(i + 1) for i in range(TOTAL_MOTOS // 10)] for _ in range(3))
    return parqueadero

# Mostrar matriz del parqueadero
def mostrar_parqueadero(parqueadero):
    print("***************************************")
    for fila in parqueadero:
        print('-'.join(fila))
    print("***************************************")

# Alquilar espacio
def alquilar_espacio(parqueadero):
    for i in range(len(parqueadero)):
        for j in range(len(parqueadero[i])):
            if parqueadero[i][j] == 'v' + str(j + 1) or parqueadero[i][j] == 'm' + str(j + 1):
                parqueadero[i][j] = 'A'
                print(f"Espacio alquilado: {parqueadero[i][j]}")
                return
    print("No hay espacios disponibles para alquilar.")

# Registrar entrada de un vehículo
def registrar_entrada(parqueadero, placas, tipo, hora):
    for i in range(len(parqueadero)):
        for j in range(len(parqueadero[i])):
            if parqueadero[i][j] == tipo + str(j + 1):
                parqueadero[i][j] = 'O'
                print(f"Vehículo registrado: {placas} en {parqueadero[i][j]} a las {hora.strftime('%H:%M')}")
                return
    print("Espacio no disponible.")

# Registrar salida de un vehículo y calcular tarifa
def registrar_salida(parqueadero, placas, tipo, hora_salida):
    for i in range(len(parqueadero)):
        for j in range(len(parqueadero[i])):
            if parqueadero[i][j] == 'O':
                hora_entrada = datetime.datetime.now()  # Suponiendo que guardamos la hora de entrada
                duracion = (hora_salida - hora_entrada).seconds // 3600 + 1  # horas
                tarifa = duracion * TARIFA_HORA
                
                if duracion >= DURACION_JORNADA * 0.7:
                    tarifa *= (1 - DESCUENTO)

                parqueadero[i][j] = tipo + str(j + 1)
                print(f"Vehículo {placas} salió de {parqueadero[i][j]}. Tarifa a pagar: {tarifa:.2f}")
                return
    print("No se encontró el vehículo.")

# Menú principal
def menu():
    parqueadero = inicializar_parqueadero()
    while True:
        print("\nMenú:")
        print("1. Mostrar matriz del parqueadero")
        print("2. Alquilar espacio")
        print("3. Registrar entrada de vehículo")
        print("4. Registrar salida de vehículo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_parqueadero(parqueadero)
        elif opcion == '2':
            alquilar_espacio(parqueadero)
        elif opcion == '3':
            placas = input("Ingrese placa del vehículo: ")
            tipo = input("Ingrese tipo (v para vehículo, m para moto): ")
            hora = datetime.datetime.now()
            registrar_entrada(parqueadero, placas, tipo, hora)
        elif opcion == '4':
            placas = input("Ingrese placa del vehículo: ")
            tipo = input("Ingrese tipo (v para vehículo, m para moto): ")
            hora_salida = datetime.datetime.now()
            registrar_salida(parqueadero, placas, tipo, hora_salida)
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
