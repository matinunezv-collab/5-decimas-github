def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_titulo(titulo):
    return titulo.strip() != ""

def buscar_libro(libros, codigo):
    for libro in libros:
        if libro["codigo"] == codigo:
            return libro
    return None

#REGISTRAR LIBRO
def registrar_libro(libros):
    print("\n===== REGISTRAR LIBRO =====")

    codigo = input("Ingrese código del libro: ").strip()

    #Validar Código
    if not validar_codigo(codigo):
        print("Error: El código no puede estar vacio")
        return
    
    #validar código único      
    if buscar_libro(libros,codigo) is not None:
        print("Error: El código ya existe")
        return
    
    titulo = input("Ingrese Título del Libro: ").strip()

    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacio.")
        return
    
    try:
        cantidad = int(input("Ingrese cantida de Libros: "))

        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return

    estado = "Disponible"

    libro = {"codigo": codigo,
             "titulo": titulo,
             "cantidad": cantidad,
             "estado" : estado}

    libros.append(libro)

    print("Libro registrado correctamente")

#Mostrar Libros
def mostrar_libros(libros):
    print("\n===== LISTADO DE LIBROS =====")

    if len(libros) == 0:
        print("No exiten libros registrados")
        return
    
    for libro in libros:
        print("========================")
        print("Código   : ",libro["codigo"])    
        print("Título   : ",libro["titulo"])
        print("Cantidad : ",libro["cantidad"])
        print("Estado   : ",libro["estado"])
    
#Actualizar Estado
def actualizar_estado(libros):
    print("\n===== ACTUALIZAR ESTADO =====")

    codigo = input("Ingrese código del Libro: ").strip()

    libro = buscar_libro(libros, codigo)

    if libro is None:
        print("Libro no Encontrado")
        return
    
    try:
        nueva_cantidad = int(input("Ingrese nueva cantidad de Libros: "))

        if nueva_cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return
        
    except ValueError:
        print("Debe Ingresar un número entero.")
        return
    
    libro["cantidad"] = nueva_cantidad

    if nueva_cantidad == 0:
        libro["estado"] = "Agostado"
    else:
        libro["estado"] = "Disponible"

    print("Estado actualizado correctamente")
    print("Nuevo Estado: ", libro["estado"])

#Mostrar Menú
def mostrar_menu():
    print("\n====== BIBLIOTECA ======")
    print("1.- Registrar Libro")
    print("2.- Mostrar Libros")
    print("3.- Actualizar Estado")
    print("4.- Salir")

#Leer Opción
def leer_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion >= 1 and opcion <= 4:
            return opcion
        
        print("Opción fuera de rango.")
        return 0
    
    except ValueError:
        print("Debe Ingresar un número.")
        return 0

#Programa Principal 
def main():

    libros = [] 

    while True:
        mostrar_menu()

        opcion = leer_opcion()

        if opcion == 1:
            registrar_libro(libros)

        elif opcion == 2:
            mostrar_libros(libros)

        elif opcion == 3:
            actualizar_estado(libros)
        
        elif opcion == 4:
            print("Programa Finalizado")
            break

main()        


