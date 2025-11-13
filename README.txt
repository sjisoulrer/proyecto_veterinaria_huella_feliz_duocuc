Huella Feliz - Sistema de Veterinaria

Huella Feliz es un programa en Python que permite gestionar información de mascotas y sus atenciones veterinarias.
Incluye un menú para registrar, modificar, eliminar y listar mascotas, registrar atenciones y exportar o importar datos en formato CSV.

------------------------------------------------------------
Estructura del proyecto
------------------------------------------------------------
huella_feliz/
│
├── menu.py          # Archivo principal con el menú del sistema
├── funciones.py     # Contiene las funciones llamadas desde el menú
├── mascotas.csv     # Archivo CSV generado al exportar los datos
└── README.txt       # Este archivo

------------------------------------------------------------
Cómo ejecutar el programa
------------------------------------------------------------
1. Asegúrate de tener Python 3 instalado.
2. Guarda los archivos menu.py y funciones.py en la misma carpeta.
3. Abre una terminal o consola en esa carpeta.
4. Ejecuta el programa con:

    python menu.py

------------------------------------------------------------
Opciones del menú principal
------------------------------------------------------------
1.- Registrar mascota
2.- Modificar mascota
3.- Eliminar mascota
4.- Listar mascotas
5.- Registrar atención veterinaria
6.- Reporte de gastos por RUT
7.- Exportar / importar datos CSV
8.- Salir

------------------------------------------------------------
Exportar / Importar datos (opción 7)
------------------------------------------------------------
- Exportar CSV: guarda las mascotas registradas en el archivo mascotas.csv.
- Importar CSV: carga los datos desde el archivo mascotas.csv si existe.

------------------------------------------------------------
Ejemplo del archivo mascotas.csv
------------------------------------------------------------
Nombre,Especie,RUT dueño
Toby,Perro,12345678-9
Mia,Gato,98765432-1
Rocky,Perro,11222333-4
Nina,Conejo,77665544-2

------------------------------------------------------------
Ejemplo de uso
------------------------------------------------------------
Bienvenido a Huella Feliz
Tu veterinaria de confianza
Seleccione una opción: 1
Nombre de la mascota: Toby
Especie: Perro
RUT del dueño: 12345678-9
Mascota registrada correctamente.

------------------------------------------------------------
Requisitos
------------------------------------------------------------
- Python 3.x
- Librería estándar csv (incluida con Python)

------------------------------------------------------------
Autor
------------------------------------------------------------
Proyecto educativo de programación en Python.
Puede modificarse o ampliarse según las necesidades del usuario.
