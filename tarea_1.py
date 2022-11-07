import csv

class Libro:
    def __init__(self,id,titulo,genero,isbn,editorial,autor_es=[]) -> None:
        self.id=id
        self.titulo=titulo
        self.genero=genero
        self.isbn=isbn
        self.editorial=editorial
        self.autor_es=autor_es

    def __str__(self) -> str:
        return f"\nTITULO\t\t {self.titulo}\n" \
               f"GENERO\t\t {self.genero}\n" \
               f"ISBN\t\t {self.isbn}\n" \
               f"EDITORIAL\t {self.editorial}\n" \
               f"AUTOR(ES)\t {self.autor_es} \n" \


def intro():
    print('\n\tBienvenido al Registro de Libros')
    print('\nElige una de estas opciones:\n')
    print('1 -> Leer archivo \n2 -> Listar libros\n3 -> Agregar libro\n4 -> Eliminar libro\n5 -> Buscar libro por ISBN o por título\n6 -> Ordenar libros por título\n7 -> Buscar libros por autor, editorial o género\n8 -> Buscar libros por número de autores\n9 -> Editar o actualizar datos de un libro\n10 -> Guardar libros en archivo\n')

    while True:
        try:
            eleccion=int(input('Eliga el [NUMERO] a Eleccion :  '))
            while eleccion not in (1,2,3,4,5,6,7,8,9,10):
                eleccion=int(input('Eliga el [NUMERO] a Eleccion : '))
            break
        except ValueError:
             print('Solo numeros!')

    listaintro=['leer','listar','add','remove','bisbn','otitulos','bautor','nautor','edit','save']
    return listaintro[eleccion-1]


def abrir_fichero():
    nom_fichero=input("ingrese el nombre del archivo->  ")
    list_lib=[]
    with open(nom_fichero,'r+') as f:
        reader = csv.reader(f)
        for item in reader:
            list_lib.append(Libro(item[0],item[1],item[2],item[3],item[4],item[5:]))

    return list_lib



def listarlibros(argumeto):
    for i in argumeto:
        print(i)
