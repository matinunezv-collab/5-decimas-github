#Funciones

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def buscar_reserva(reservas, codigo):
    for reserva in reservas:
        if reserva["codigo"] == codigo:
            return reserva
    return None

#Registrar Reserva
def registrar_reserva(reservas):
    codigo = input("Ingrese codigo de reserva: ").strip()

    if not validar_codigo(codigo):
        print("El codigo no puede estar vacío. Reintente")
        return
    
    if buscar_reserva(reservas, codigo) is not None:
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

    total = noches * valor_noche
    if total < 200000:
        categoria = "Económica"
    elif total > 200000 and total <500000:
        categoria = "Estándar"
    elif total > 500000:
        categoria = "Premium"

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

    if buscar in reservas:
        print("Reserva Encontrada")
        for i, reserva in enumerate(reservas, start=1):
            print(i, reserva)
            print("Codigo   : ",reserva["codigo"])
            print("Nombre   : ",reserva["nombre"])
            print("Noches   : ",reserva["noches"])
            print("Valor por noche  : ",reserva["valor por noche"])
            print("Total    :",reserva["total"])
            print("Categoría    : ",reserva["categoría"])
            return
    else:
        print("Reserva no encontrada")
        return
    
def actualizar_reserva(reservas):

    codigo = input("Ingrese codigo de reserva: ").strip()

    reserva = buscar_reserva(reservas,codigo)

    if reserva is None:
        print("Reserva no encontrada")
        return
    else:
        reservas

#Menu

print("====== MENÚ DE RESERVA ======")
print("1. Registrar Reserva")
print("2. Buscar Reserva")
print("3. Actualizar Reserva")
print("4. Eliminar Reserva")
print("5. Mostrar Reserva")
print("6. Mostrar Estadísticas")
print("7. Salir")


