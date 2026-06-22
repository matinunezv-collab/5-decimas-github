#Funciones

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def buscar_reserva_por_codigo(reservas, codigo):
    for reserva in reservas:
        if reserva["codigo"] == codigo:
            return reserva
    return None

def buscar_posicion_reserva(reservas, codigo):
    for i, reserva in enumerate(reservas):
        if reserva["codigo"] == codigo:
            return i
    return -1

def mostrar_datos_reserva(reserva):
    print("Codigo   : ", reserva["codigo"])
    print("Nombre   : ", reserva["nombre"])
    print("Noches   : ", reserva["noches"])
    print("Valor por noche  : ", reserva["valor por noche"])
    print("Total    : ", reserva["total"])
    print("Categoría    : ", reserva["categoría"])

def calcular_categoria(total):
    if total < 200000:
        categoria = "Económica"
    elif total >= 200000 and total <= 500000:
        categoria = "Estándar"
    else:
        categoria = "Premium"

    return categoria


#Registrar Reserva
def registrar_reserva(reservas):
    codigo = input("Ingrese codigo de reserva: ").strip()

    if not validar_codigo(codigo):
        print("El codigo no puede estar vacío. Reintente")
        return
    
    if buscar_reserva_por_codigo(reservas, codigo) is not None:
        print("El codigo ya existe, ingrese uno nuevo.")
        return
    
    nombre = input("Ingrese nombre del huesped: ").strip()

    if not validar_nombre(nombre):
        print("El nombre no puede estar vacío")
        return
    
    try:
        noches = int(input("Ingrese cantidad de noches: "))

        if noches <= 0:
            print("Ingrese una cantidad mayor a 0")
            return
    except ValueError:
        print("Error, el número debe ser un entero")
        return
    
    try:
        valor_noche = int(input("Ingrese el valor por noche: "))

        if valor_noche <= 0:
            print("El valor por noche debe ser mayor a 0")
            return
            
    except ValueError:
        print("Error, ingrese un numero entero")
        return

    total = noches * valor_noche
    categoria = calcular_categoria(total)

    reserva = {"codigo": codigo,
               "nombre": nombre,
               "noches": noches,
               "valor por noche": valor_noche,
               "total": total,
               "categoría": categoria}
    
    reservas.append(reserva)

    print("Reserva registrada correctamente")


def buscar_reserva(reservas):
    buscar = input("Ingrese codigo de reserva: ").strip()

    reserva = buscar_reserva_por_codigo(reservas, buscar)

    if reserva is not None:
        posicion = buscar_posicion_reserva(reservas, buscar)

        print("Reserva Encontrada")
        print("Posición: ", posicion)
        mostrar_datos_reserva(reserva)

    else:
        print("Reserva no encontrada")
        return
    

def actualizar_reserva(reservas):

    codigo = input("Ingrese codigo de reserva: ").strip()

    reserva = buscar_reserva_por_codigo(reservas, codigo)

    if reserva is None:
        print("Reserva no encontrada")
        return
    else:
        print("Reserva encontrada. Datos actuales:")
        mostrar_datos_reserva(reserva)

        nuevo_nombre = input("Ingrese nuevo nombre del huesped: ").strip()

        if not validar_nombre(nuevo_nombre):
            print("El nombre no puede estar vacío")
            return
        
        try:
            nuevas_noches = int(input("Ingrese nueva cantidad de noches: "))

            if nuevas_noches <= 0:
                print("Ingrese una cantidad mayor a 0")
                return
        except ValueError:
            print("Error, el número debe ser un entero")
            return
        
        try:
            nuevo_valor_noche = int(input("Ingrese nuevo valor por noche: "))

            if nuevo_valor_noche <= 0:
                print("El valor por noche debe ser mayor a 0")
                return
            
        except ValueError:
            print("Error, ingrese un numero entero")
            return
        
        nuevo_total = nuevas_noches * nuevo_valor_noche
        nueva_categoria = calcular_categoria(nuevo_total)

        reserva["nombre"] = nuevo_nombre
        reserva["noches"] = nuevas_noches
        reserva["valor por noche"] = nuevo_valor_noche
        reserva["total"] = nuevo_total
        reserva["categoría"] = nueva_categoria

        print("Reserva actualizada correctamente")


def eliminar_reserva(reservas):
    codigo = input("Ingrese codigo de reserva a eliminar: ").strip()

    posicion = buscar_posicion_reserva(reservas, codigo)

    if posicion == -1:
        print("Reserva no encontrada")
        return
    else:
        reservas.pop(posicion)
        print("Reserva eliminada correctamente")


def mostrar_reservas(reservas):
    if len(reservas) == 0:
        print("No hay reservas registradas")
        return
    
    for i, reserva in enumerate(reservas, start=1):
        print("\nReserva N°", i)
        mostrar_datos_reserva(reserva)


def mostrar_estadisticas(reservas):
    if len(reservas) == 0:
        print("No hay reservas registradas para mostrar estadísticas")
        return
    
    cantidad_total = len(reservas)
    ingresos_totales = 0

    for reserva in reservas:
        ingresos_totales = ingresos_totales + reserva["total"]

    reserva_mayor = reservas[0]

    for reserva in reservas:
        if reserva["total"] > reserva_mayor["total"]:
            reserva_mayor = reserva

    promedio = ingresos_totales / cantidad_total

    print("Cantidad total de reservas: ", cantidad_total)
    print("Ingresos totales: ", ingresos_totales)
    print("Promedio de ingresos por reserva: ", promedio)

    print("\nReserva de mayor valor:")
    mostrar_datos_reserva(reserva_mayor)


def mostrar_menu():
    print("\n====== MENÚ DE RESERVA ======")
    print("1. Registrar Reserva")
    print("2. Buscar Reserva")
    print("3. Actualizar Reserva")
    print("4. Eliminar Reserva")
    print("5. Mostrar Reserva")
    print("6. Mostrar Estadísticas")
    print("7. Salir")


def ejecutar_programa():
    reservas = []

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Ingrese una opción: "))

            if opcion == 1:
                registrar_reserva(reservas)

            elif opcion == 2:
                buscar_reserva(reservas)

            elif opcion == 3:
                actualizar_reserva(reservas)

            elif opcion == 4:
                eliminar_reserva(reservas)

            elif opcion == 5:
                mostrar_reservas(reservas)

            elif opcion == 6:
                mostrar_estadisticas(reservas)

            elif opcion == 7:
                print("Gracias por utilizar el sistema. Hasta pronto")
                break

            else:
                print("Opción inválida. Debe ingresar un número entre 1 y 7")

        except ValueError:
            print("Error, debe ingresar un número entero")


ejecutar_programa()