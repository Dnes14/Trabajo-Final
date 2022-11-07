import csv
import os

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
    print('1 -> Leer archivo \n2 -> Listar libros\n3 -> Agregar libro\n4 -> Eliminar libro\n5 -> Buscar libro por ISBN o por título\n6 -> Ordenar libros por título\n7 -> Buscar libros por autor, editorial o género\n8 -> Buscar libros por número de autores\n9 -> Editar o actualizar datos de un libro\n10 -> Guardar libros en archivo\n11-> Salir')

    while True:
        try:
            eleccion=int(input('Eliga el [NUMERO] a Eleccion :  '))
            while eleccion not in (1,2,3,4,5,6,7,8,9,10,11):
                eleccion=int(input('Eliga el [NUMERO] a Eleccion : '))
            break
        except ValueError:
             print('Solo numeros!')

    listaintro=['leer','listar','add','remove','bisbn','otitulos','bautor','nautor','edit','save','salir']
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

def agregarlibro(id,List3):

    autores=[]   
    nom=input("\nIngrese el [TITULO] del Libro:\t\t\t ")
    gene=input("\nIngrese el [GENERO] del Libro:\t\t\t ")
    IS=input("\nIngrese el [ISBN] del Libro:\t\t\t ")
    Edit=input("\nIngrese la [EDITORIAL] del Libro:\t\t ")
    cant=input("\nIngrese la [Cantidad] de Autores:\t\t ")

    if int(cant)>1:
        for i in range (cant):
            auts=input(f"\nIngrese el autor N:{i+1} :\t\t ")
            autores.append(auts)
    elif int(cant)==1:
        auts=input("\nIngrese el autor :\t\t ")
        autores.append(auts)
    else:
        autores.append("Desconocido")
                
    List3.append(Libro(id,nom,gene,IS,Edit,autores))
    return List3
    
def sacar_libro(lista2):
    print('Eliga la opcion para sacar el libro')

    a=0
    for item in lista2:

        print(lista2[a].id,"-->",lista2[a].titulo)
        a=a+1

    retira=input('numero de id a retirar')
   # index = lista2.id.index(retira)
    a=0
    for item in lista2:

        if lista2[a].id==retira:
          lista2.pop(a)  
        a=a+1

    return lista2

def Buscar_libro(listb):
    print("Buscar em datos")

    buscar=input('numero de id a retirar: ')

    a=0
    for item in listb:

        if (listb[a].titulo or listb[a].ISBM)==buscar:
          print(listb[a])  
        a=a+1


def ordenar_libros(listb):
    orden=(sorted(listb,key=lambda x: x.titulo))
    for i in orden:
        print(i)
   

def guardar_archivo(listb):
    nom_fichero=input("ingrese el nombre del archivo->  ")
    f = open(nom_fichero,'w') 

    a=0
    for item in listb:
        b=f"{listb[a].id},{listb[a].titulo},{listb[a].isbn},{listb[a].editorial},{','.join(listb[a].autor_es)}"
        f.write(b)
        f.write("\n")
        a=a+1
    f.close



while True:

    inicio=intro()

    while inicio != 'salir':

        if inicio == 'leer':
            lib=abrir_fichero()
            input("\nPresione [Enter] para continuar... ")
            os.system('cls')
            break
                
        elif inicio == 'listar':
            listarlibros(lib)
            input("\nPresione [Enter] para continuar... ")
            os.system('cls')
            break
            
        elif inicio == 'add':
            id=input('Ingrese el ID :')
            agregarlibro(id,lib)
            input("\nPresione [Enter] para continuar... ")
            os.system('cls')
            break

        elif inicio == 'remove':
            sacar_libro(lib)
            input("\nPresione [Enter] para continuar... ")
            os.system('cls')
            break

        elif inicio == 'bisbn':
            Buscar_libro(lib)
            input("\nPresione [Enter] para continuar... ")
            os.system('cls')
            break

        elif inicio == 'otitulos':
            ordenar_libros(lib)
            input("\nPresione [Enter] para continuar... ")
            os.system('cls')
            break

        elif inicio == 'bautor':
            pass

        elif inicio == 'nautor':
            pass

        elif inicio == 'edit':
            pass

        elif inicio == 'save':
            guardar_archivo(lib)
            input("\nPresione [Enter] para continuar... ")
            os.system('cls')
            break    
    
    if inicio=='salir':
        break



