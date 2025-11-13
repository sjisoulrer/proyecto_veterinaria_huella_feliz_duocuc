import csv

mascotas = {}
atenciones = []

def registrar_mascota():
    rut = input("Ingrese su rut del dueño: ")
    nombre = input("Ingresa nombre de la mascota(pacientes): ")
    
    clave = rut + "-" + nombre.lower()
    if clave  in mascotas:
        print("el paciente/mascota ya se encuentra registrada")
        return
    
    
    especie = input("Ingrese especie(perro, gato, etc): ")
    edad = input("Ingrese edad: ")
    
    mascotas[clave] = {"rut": rut, "nombre": nombre, "especie": especie, "edad": edad}
    print("Mascota registrada con exito")


def actualizar_mascota():
    clave = input("Ingrese rut + nombre de mascota (ejemplo: 21943166-k_chico): ").lower()
    if clave not in mascotas:
        print("La mascota no se encuentra registrada")
        return
    
    nueva_edad = input("Ingrese nueva edad de la mascota: ")
    mascotas[clave]["edad"] = nueva_edad
    print("Mascota actualizada")

def eliminar_mascota():
    eliminar = input("Ingrese rut + nombre de mascota (ej: 21943166-k_firulais):  ").lower().strip()
    
    if eliminar in mascotas:
        del mascotas[eliminar]
        print("Mascotas eliminada con exito")        
    else:
        print("No se encontro ninguna mascota registrada con esos datos")

def listar_mascota():
    if not mascotas:
        print("No se encuentran mascotas registradas")
        return
    
    print("***Lista de mascotas resgistradas***")
    for clave, datos in mascotas.items():
        print(f"Rut dueño: {datos['rut']}")
        print(f"Nombre Mascota: {datos['nombre']}")
        print(f"Especie: {datos['especie']}")
        print(f"Edad: {datos['edad']} años")
        print("-" * 30)
        
def registrar_atencion():
    rut = input("Ingrese rut del dueño: ").strip()
    nombre = input("Ingrese nombre de la mascota: ").strip().lower()
    clave = rut + "-"+ nombre
    
    if clave not in mascotas:
        print("La mascota no se encuentra registrada")
        print("Registrelo primero usando la opcion (1)")
        return
    
    fecha = input("Ingrese fecha de atencion (ej: 20-04-2025): ").strip()
    descripcion = input("Ingrese descripcion de la atencion:  ").strip()
    costo = input("Ingrese costo de la antencion: ").strip()
    
    
    try:
        costo = float(costo)
    except ValueError:
        print("El costo debe ser un numero.")
        return
    
    n_atencion = {
        "clave": clave,
        "fecha": fecha,
        "descripcion": descripcion,
        "costo": costo
    }
    atenciones.append(n_atencion)
    print("Atencion registrada exitosamente")
    
def reporte_gastos():
    rut = input("Ingrese Rut del dueño: ").strip()
    total = 0
    
    for atencion in atenciones:
        if atencion["clave"][:len(rut)] == rut:
            total += atencion["costo"]
            
    print(f"El rut:{rut} tiene un gasto total de: ${total:.2f}")
    
def exportar_datos_csv():
    with open("mascotas.csv", mode="w", newline="") as archivo_mascotas:
        campos = ["rut", "nombre", "especie", "edad"]
        escritor = csv.DictWriter(archivo_mascotas, fieldnames=campos)
        escritor.writeheader()
        for datos in mascotas.values():
            escritor.writerow(datos)
    
    with open("atenciones.csv", mode="w", newline="") as archivo_atenciones:
        campos = ["clave", "fecha", "descripcion", "costo"]
        escritor = csv.DictWriter(archivo_atenciones, fieldnames=campos)
        escritor.writeheader()
        for atencion in atenciones:
            escritor.writerow(atencion)
    
    print("Datos exportados a mascotas.csv y atenciones.csv")   
    
def importar_datos_csv():
    try:
        with open("mascotas.csv", mode="r") as archivo_mascotas:
            lector = csv.DictReader(archivo_mascotas)
            for fila in lector:
                clave = fila["rut"] + "-" + fila["nombre"].lower()
                mascotas[clave] = {
                    "rut": fila["rut"],
                    "nombre": fila["nombre"],
                    "especie": fila["especie"],
                    "edad": fila["edad"]
                }
        
        with open("atenciones.csv", mode="r") as archivo_atenciones:
            lector = csv.DictReader(archivo_atenciones)
            for fila in lector:
                atencion = {
                    "clave": fila["clave"],
                    "fecha": fila["fecha"],
                    "descripcion": fila["descripcion"],
                    "costo": float(fila["costo"])
                }
                atenciones.append(atencion)
        
        print("Datos importados exitosamente desde mascotas.csv y atenciones.csv")
    except FileNotFoundError:
        print("No se encontraron los archivos mascotas.csv o atenciones.csv")

