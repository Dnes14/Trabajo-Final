import os
import time
import requests
import json

url_pokeapi = 'https://pokeapi.co/api/v2/'

def intro():
    print('\n\tBienvenido al mundo POKEMON')
    print('\nElige una de estas opciones:\n')
    print('1 -> Por Generación\t\t2 -> Por Color\n3 -> Por Habilidad\t\t4 -> Por Hábitat\n5 -> Por Tipo\t\t\t0 -> [Salir]\n')
    
    while True:
        try:
            eleccion=int(input('Eliga el [NUMERO] a Eleccion :   '))
            while eleccion not in (0,1,2,3,4,5):
                eleccion=int(input('Eliga el [NUMERO] a Eleccion :   '))
            break
        except ValueError:
             print('Solo numeros!')

    listaintro=['Exit','generation','pokemon-color','ability','pokemon-habitat','type']
    return listaintro[eleccion]

def obt_opciones(ra):
    response=requests.get(url_pokeapi+ra)

    data = response.json()
    lista_nombre = [lista_nombre['name'] for lista_nombre in data['results']]
    b=0
    for a in lista_nombre:
        print(f'{b+1} -> {lista_nombre[b]}')
        b=b+1
    #eleccion=int(input('Eliga el [NUMERO] a Eleccion :   '))
    while True:
        try:
            eleccion=int(input('Eliga el [NUMERO] a Eleccion :   '))
            while eleccion not in range(b+1):
                eleccion=int(input('Eliga el [NUMERO] a Eleccion :   '))
            break
        except ValueError:
             print('Solo numeros!')

    return lista_nombre[eleccion-1]

def mostrar_op1_2_4(pi,ka):
    response=requests.get(url_pokeapi+pi+"/"+ka)

    data= response.json()
    #print(data)
    limpiaurl = 'https://pokeapi.co/api/v2/pokemon-species/'
    pokem = [pokem['url'].replace(limpiaurl,'') for pokem in data['pokemon_species']]

    numpoke=[]
    for i in pokem:
        a=i.replace("/",'')
        numpoke.append(int(a))
    
    return sorted(numpoke)
    
