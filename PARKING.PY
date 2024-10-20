import datetime
import csv
import os

# Constantes
TOTAL_VEHICULOS = 50  # 50 espacios para carros
TOTAL_MOTOS = 30       # 30 espacios para motos
TARIFA_HORA = 2000     # Tarifa por hora
TARIFA_DIARIA = 16000  # Tarifa por día
DURACION_MINIMA = 8    # Días mínimos para desocupar
CSV_FILE_PATH = r"C:\Users\duver\Documents\python\PARKING_INF.CSV"

# Inicialización de parqueadero
def inicializar_parqueadero():
    parqueadero = {}
    for i in range(1, TOTAL_VEHICULOS + 1):
        parqueadero[f'Espacio C{str(i).zfill(2)}'] = {'tipo': 'v', 'estado': 'libre', 'placa': None, 'hora_entrada': None, 'tipo_cobro': None}
    
    for i in range(1, TOTAL_MOTOS + 1):
        parqueadero[f'Espacio M{str(i).zfill(2)}'] = {'tipo': 'm', 'estado': 'libre', 'placa': None, 'hora_entrada': None, 'tipo_cobro': None}
    
    return parqueadero

# Cargar datos desde archivo CSV
def cargar_datos(file_path=CSV_FILE_PATH):
    parqueadero = inicializar_parqueadero()
    if os.path.exists(file_path):
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    espacio = row['Espacio']
                    parqueadero[espacio] = {
                        'tipo': row['Tipo'],
                        'estado': row['Estado'],
                        'placa': row['Placa'],
                        'hora_entrada': datetime.datetime.strptime(row['Hora Entrada'], '%Y-%m-%d %H:%M') if row['Hora Entrada'] else None,
                        'tipo_cobro': row['Tipo Cobro']
                    }
        except Exception as e:
            print(f"Error al cargar datos: {e}")
    return parqueadero

# Guardar datos en archivo CSV
def guardar_datos(parqueadero, file_path=CSV_FILE_PATH):
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Espacio', 'Tipo', 'Estado', 'Placa', 'Hora Entrada', 'Tipo Cobro'])
            writer.writeheader()
            for espacio, info in parqueadero.items():
                writer.writerow({
                    'Espacio': espacio,
                    'Tipo': info['tipo'],
                    'Estado': info['estado'],
                    'Placa': info['placa'],
                    'Hora Entrada': info['hora_entrada'].strftime('%Y-%m-%d %H:%M') if info['hora_entrada'] else '',
                    'Tipo Cobro': info['tipo_cobro']
                })
    except Exception as e:
        print(f"Error al guardar datos: {e}")

# Mostrar matriz del parqueadero
def mostrar_parqueadero(parqueadero):
    print("***************************************")
    print("Matriz del Parqueadero:")
    
    # Mostrar espacios de vehículos (C)
    print("Vehículos (Carros):")
    for i in range(1, TOTAL_VEHICULOS + 1):
        espacio = f'Espacio C{str(i).zfill(2)}'
        estado = parqueadero[espacio]['estado']
        if estado == 'libre':
            print(f"C{i:02d}", end=" ")
        elif estado == 'ocupado':
            print("OOO", end=" ")
        elif estado == 'alquilado':
            print("AAA", end=" ")
        
        if i % 10 == 0:  # Nueva línea cada 10 espacios
            print()

    print("\nMotos:")
    for i in range(1, TOTAL_MOTOS + 1):
        espacio = f'Espacio M{str(i).zfill(2)}'
        estado = parqueadero[espacio]['estado']
        if estado == 'libre':
            print(f"M{i:02d}", end=" ")
        elif estado == 'ocupado':
            print("OOO", end=" ")
        elif estado == 'alquilado':
            print("AAA", end=" ")
        
        if i % 10 == 0:  # Nueva línea cada 10 espacios
            print()
    
    print("\n***************************************")

# Alquilar espacio
def alquilar_espacio(parqueadero):
    placas = input("Ingrese la placa del vehículo: ").upper()
    tipo = input("Ingrese tipo (m para moto, c para carro): ").lower()

    # Verificar si la placa ya tiene un alquiler activo
    for info in parqueadero.values():
        if info['placa'] == placas and info['estado'] == 'alquilado':
            print(f"El vehículo con placa {placas} ya tiene un alquiler activo.")
            return

    for espacio, info in parqueadero.items():
        if info['estado'] == 'libre' and info['tipo'] == ('v' if tipo == 'c' else 'm'):
            info['estado'] = 'alquilado'
            info['placa'] = placas
            info['hora_entrada'] = datetime.datetime.now()  # Registra la hora al alquilar
            info['tipo_cobro'] = input("Ingrese tipo de cobro (horas/alquiler): ").lower()
            print(f"Espacio alquilado: {espacio} para el vehículo {placas} a las {info['hora_entrada'].strftime('%H:%M')}")
            return
    print("No hay espacios disponibles para alquilar.")

# Registrar entrada de un vehículo
def registrar_entrada(parqueadero, placas):
    placas = placas.upper()
    for espacio, info in parqueadero.items():
        if info['placa'] == placas:
            print(f"El vehículo con placa {placas} ya está registrado en el parqueadero.")
            return

    tipo = input("Ingrese tipo (m para moto, c para carro): ").lower()
    
    for espacio, info in parqueadero.items():
        if info['tipo'] == ('v' if tipo == 'c' else 'm') and info['estado'] == 'libre':
            info['estado'] = 'ocupado'
            info['placa'] = placas
            info['hora_entrada'] = datetime.datetime.now()
            info['tipo_cobro'] = input("Ingrese tipo de cobro (horas/alquiler): ").lower()
            print(f"Vehículo registrado: {placas} en {espacio} a las {info['hora_entrada'].strftime('%H:%M')}")
            return
    print("Espacio no disponible.")

# Registrar salida de un vehículo y calcular tarifa
def registrar_salida(parqueadero, placas):
    placas = placas.upper()
    for espacio, info in parqueadero.items():
        if info['estado'] == 'ocupado' and info['placa'] == placas:
            hora_salida = datetime.datetime.now()
            duracion = hora_salida - info['hora_entrada']
            
            # Preguntar si desea finalizar el alquiler
            if info['tipo_cobro'] == 'alquiler':
                confirmacion = input(f"¿Desea finalizar el alquiler del vehículo {placas}? (si/no): ")
                if confirmacion.lower() == 'si':
                    duracion_dias = duracion.days
                    if duracion_dias < DURACION_MINIMA:
                        duracion_dias = DURACION_MINIMA
                    tarifa = duracion_dias * TARIFA_DIARIA
                    print(f"Vehículo {placas} salió de {espacio}. Tarifa a pagar: {tarifa:.2f}")
                    # Liberar el espacio
                    info['estado'] = 'libre'
                    info['placa'] = None
                    info['hora_entrada'] = None
                    info['tipo_cobro'] = None
                else:
                    print(f"Salida temporal registrada para el vehículo {placas}.")
            else:
                # Calcular tarifa por horas
                tarifa = (duracion.seconds // 3600 + 1) * TARIFA_HORA  # Redondear hacia arriba
                print(f"Vehículo {placas} salió de {espacio}. Tarifa a pagar: {tarifa:.2f}")
                
                # Liberar el espacio
                info['estado'] = 'libre'
                info['placa'] = None
                info['hora_entrada'] = None
                info['tipo_cobro'] = None
            return

    print("No se encontró el vehículo.")

# Consultar estado del vehículo
def consultar_estado(parqueadero):
    placa = input("Ingrese la placa del vehículo: ").upper()
    
    for espacio, info in parqueadero.items():
        if info['placa'] == placa:
            print(f"Estado del vehículo {placa}:")
            print(f"- Tipo de vehículo: {'Carro' if info['tipo'] == 'v' else 'Moto'}")
            print(f"- Espacio asignado: {espacio}")

            # Verificar si hay hora de entrada registrada
            hora_entrada = info['hora_entrada']
            if hora_entrada:
                print(f"- Fecha y hora de ingreso: {hora_entrada.strftime('%Y-%m-%d %H:%M')}")
                duracion = datetime.datetime.now() - hora_entrada
                print(f"- Tiempo en el parqueadero: {duracion}")

                # Calcular el costo
                if info['tipo_cobro'] == 'horas':
                    tarifa = (duracion.seconds // 3600 + 1) * TARIFA_HORA  # Redondear hacia arriba
                    print(f"- Valor a pagar hasta el momento: {tarifa:.2f}")
                elif info['tipo_cobro'] == 'alquiler':
                    duracion_dias = duracion.days
                    if duracion_dias < DURACION_MINIMA:
                        duracion_dias = DURACION_MINIMA
                    tarifa = duracion_dias * TARIFA_DIARIA
                    print(f"- Valor a pagar hasta el momento: {tarifa:.2f}")
            else:
                print("- Fecha y hora de ingreso: No disponible")
            
            print(f"- Estado: {'Dentro' if info['estado'] == 'ocupado' else 'Fuera (Alquilado)'}")
            return
            
    print("No se encontró el vehículo.")

# Eliminar historial del CSV
def eliminar_historial(parqueadero):
    confirmacion = input("Ingrese la clave para confirmar la eliminación del historial: ")
    if confirmacion == "ELIMINAR":
        parqueadero.clear()  # Limpiar el parqueadero
        with open(CSV_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Espacio', 'Tipo', 'Estado', 'Placa', 'Hora Entrada', 'Tipo Cobro'])  # Escribir encabezados
        print("Historial eliminado exitosamente.")
    else:
        print("Clave incorrecta. No se realizó ninguna acción.")

# Menú principal
def menu():
    parqueadero = cargar_datos()
    
    while True:
        print("\nMenú:")
        print("1. Mostrar matriz del parqueadero")
        print("2. Alquilar espacio")
        print("3. Registrar entrada de vehículo")
        print("4. Registrar salida de vehículo")
        print("5. Consultar estado del vehículo")
        print("6. Eliminar historial del CSV")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_parqueadero(parqueadero)
        elif opcion == '2':
            alquilar_espacio(parqueadero)
        elif opcion == '3':
            placas = input("Ingrese la placa del vehículo: ").upper()
            registrar_entrada(parqueadero, placas)
        elif opcion == '4':
            placas = input("Ingrese placa del vehículo: ").upper()
            registrar_salida(parqueadero, placas)
        elif opcion == '5':
            consultar_estado(parqueadero)
        elif opcion == '6':
            eliminar_historial(parqueadero)
        elif opcion == '7':
            guardar_datos(parqueadero)
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
