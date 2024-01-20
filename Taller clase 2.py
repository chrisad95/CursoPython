## frase
mi_frase = "Soy christian y mi prioridad es dormir"
print(mi_frase)

## numero de peliuclas vistas en los últimos 5 años 
numero_de_peliculas =[5,8,7,5,9]
print(numero_de_peliculas)


##diccionario peliculas favoritas

peliculas_fav = {"animada":"cars", "cienciaficcion":"starwars", "accion":"007notimetodie"}
print(peliculas_fav)


############ DECLARAR UN VECTOR DE ENTEROS
vector_enteros=[7]*10
print(vector_enteros)

vector_flotantes=[8.22]*5
print(vector_flotantes)

diccionario = {"entero" : vector_enteros, "flotante" : vector_flotantes}
print(diccionario)


#CADENAS
#SALIDAS Y MENSAJES
#CREACIÓN DE IDENTIFICADORES
cadena_simple = 'Hola a todos!'

#Comida favorita
cadena_doble=["hamburguesa","encebollado"]
print(cadena_doble)
print(cadena_simple)


# Tabla Excel usando pandas
import pandas as pd
imp_sri= pd.read_excel("ventas_SRI.xlsx")
print(imp_sri)
