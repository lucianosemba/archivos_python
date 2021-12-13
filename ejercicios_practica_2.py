# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open (archivo, "r") as csvfile:
        stock = list(csv.DictReader(csvfile))

    total_tornillos = 0

    for i in range(len(stock)):
        lista_stock = stock[i]
        for k, v in lista_stock.items():
            if k == "tornillos":
                cantidad_tornillos = v
                total_tornillos += int(cantidad_tornillos)

    print("La cantidad de tornillos es de", total_tornillos)


    


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open (archivo, "r") as csvfile:
        edificio = list(csv.DictReader(csvfile))

    dos_ambientes = 0
    tres_ambientes = 0

    for i in range(len(edificio)):
        piso = edificio[i]
        for k, v in piso.items():
            if k == "ambientes":
                if "2" in v:
                    dos_ambientes += 1
                elif "3" in v:
                    tres_ambientes += 1

    print("Hay", dos_ambientes, "departamentos de 2 ambientes y", tres_ambientes, "de 3 ambientes")



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
