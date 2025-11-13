import funciones

while True:
    print("Bienvenido a Huella Feliz")
    print("Tu veterinaria de confianza")
    print("1.-Registrar mascota")
    print("2.-Modificar mascota")
    print("3.-Eliminar mascota")
    print("4.-Listar mascotas")
    print("5.-Registrar atencion veterinaria")
    print("6.-Reporte de gastos por rut")
    print("7.-Exportar/importar datos CSV")
    print("8.-Salir")
        
    op = input("Seleccione una opcion: ")
        
    if op == "1":
        funciones.registrar_mascota()
    if op == "2":
        funciones.actualizar_mascota()
    if op == "3":
        funciones.eliminar_mascota()
    if op == "4":
        funciones.listar_mascota()
    if op == "5":
        funciones.registrar_atencion()
    if op == "6":
        funciones.reporte_gastos()
    if op == "7":
        print("1.- Exportar datos a CSV")
        print("2.- Importar datos desde CSV")
        op = input("Seleccione una opcion: ")
        if op == "1":
            funciones.exportar_datos_csv()
        if op == "2":
            funciones.importar_datos_csv()
    if op == "8":
        print("Gracias por usar Huella Feliz")
        break
            