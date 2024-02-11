#1.	Encuentra y muestra por pantalla qué caracter ocupa la 3 posición dentro de la siguiente palabra: “escritorio”.

"""
palabra="escritorio"
resultado=palabra[2]
print(resultado)

"""

#2.	Muestra por pantalla el índice de la primera aparición de la palabra “videojuego” en la siguiente frase: “No es por nada, pero este videojuego es demasiado fácil”.

"""
palabra="No es por nada, pero este videojuego es demasiado fácil".find("videojuego")
print(palabra)

"""

#3.	Muestra por pantalla el índice de la última aparición de la palabra “ejercicio” en la siguiente frase: “Tengo que asegurarme de comprobar el ejercicio para que no tenga errores”.

"""
palabra="Tengo que asegurarme de comprobar el ejercicio para que no tenga errores".rfind("ejercicio")
print(palabra) 

"""

#4.	Extrae la primera palabra de la siguiente frase usando slicing, y muéstrala por pantalla: “Escribir código es fundamental para aprender programación”.

"""
palabra="Escribir código es fundamental para aprender programación"
resultado=palabra.split()
print(resultado[0])

"""

#5.	Coge cada tercer caracter empezando desde el sexto hasta el final de la frase, e imprime el resultado: “Python es uno de los lenguajes más populares de la actualidad”.

"""
palabra="Python es uno de los lenguajes más populares de la actualidad"
resultado=palabra[2::6]
print(resultado)

"""

#6.	Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado por pantalla: “Si trabajas con ordenadores no tienes que aguantar discusiones ni bromas estúpidas, además de que no se comen tu comida”.

"""
palabra="Si trabajas con ordenadores no tienes que aguantar discusiones ni bromas estúpidas, además de que no se comen tu comida"
resultado=palabra[::-1]
print(resultado)

"""

#7.	Imprime el siguiente texto en mayúsculas, usando métodos de strings. “Con estos ejercicios voy a adquirir todo lo necesario para dominar la lógica de programación”.

"""
palabra="Con estos ejercicios voy a adquirir todo lo necesario para dominar la lógica de programación"
resultado= palabra.upper() 
print(resultado)

"""
#8.	Dada la siguiente lista(palabras = ["Este", "curso", "me", "gusta"]), únela completa en un string, separando cada elemento con un espacio. Usa métodos específicos para ello, y muestra el resultado por pantalla:

"""
palabras=" "
resultado=palabras.join(["Este", "curso", "me", "gusta"])
print(resultado)

"""
#9.	Haz reemplazos en la siguiente frase: “No sé con cuál quedarme, si con el primero o con el segundo”. Debes cambiar “el primero” por “JavaScript” y “el segundo” por “Python”. Muestra el resultado por pantalla.

"""
palabras="No sé con cuál quedarme, si con el primero o con el segundo"
primero=palabras.replace("el primero", "JavaScript")
segundo=primero.replace("el segundo", "Python")
print(segundo)

"""

#10.	Verifica si la palabra “trabajo” no se encuentra en la siguiente frase. Debes imprimir el booleano: “Mi jefe me ha mandado aprender Python para el trabajo, y estoy emocionado”.

"""
palabras="Mi jefe me ha mandado aprender Python para el trabajo, y estoy emocionado".find("trabajo")

print(palabras >=0)

"""

#11.	Concatena 12 veces la palabra “Python” y muestra el resultado por pantalla. Recuerda que los strings son multiplicables.

"""
palabra="Python"
print(palabra*5)

"""

#12.	Muestra el largo de la palabra “esternocleidomastoideo”. Hazlo por pantalla y con el número de caracteres.

"""
palabra="esternocleidomastoideo"
print(len(palabra))

"""

#13.	Crea una lista con 8 elementos, dentro de la variable “lista”. Puedes incluir los tipos de datos que quieras. Muéstrala por pantalla.

"""
lista=[1,2,3,4,5,6,7,8]
print(lista)

"""

#14.	Agrega el elemento “JavaScript” a la siguiente lista(lenguajes = ["Python", "Ruby", "PHP", "CSS"]) (No modifiques la línea de código dada, sino que debes usar métodos apropiados para listas).

"""
lenguajes = ["Python", "Ruby", "PHP", "CSS"]
lenguajes.append("JavaScript")
print(lenguajes)

"""

#15.	Usa el método pop() para quitar el quinto elemento de la siguiente lista (marcas = ["Acer", "Samsung", "Xiaomi", "Apple", "Windows", "LG"]) llamada marcas, y almacénalo en una variable llamada “eliminada”. Usa métodos de listas para no alterar la línea de código:

"""
marcas = ["Acer", "Samsung", "Xiaomi", "Apple", "Windows", "LG"]
eliminada=marcas.pop(4)
print(marcas,eliminada)

"""

#16.	Crea un diccionario que almacene la siguiente información: Tu nombre, tu primer apellido, tu edad y tu profesión.

"""
nombre=input("Por favor, dígame como se llama: ")
apellido=input("Ahora, dígame su primer apellido: ")
edad=input(f"Muchas gracias, {nombre} {apellido}. ¿Me podria indicar su edad, por favor?: ")
profesion=input("Por último, indique su profesión actual: ")

diccionario={1:nombre,2:apellido,3:edad,4:profesion}
print(f"Muchas gracias por todo. Aquí le mostramos una lista de los datos introducidos: {diccionario}")


#17.	Usa print para que devuelva el segundo ítem del diccionario que creaste antes. Muéstralo por pantalla, y deberás asegurarte de que, si cambia el código te siga mostrando el valor almacenado en dicha clave.


print(diccionario[2])

"""

#18.	Dado el siguiente diccionario:diccionario = {"nombre": "Juan Carlos", "Apellido": "Fernández", "Edad": 28} 
# Añade una clave que sea "país", sin tilde, y dale el valor que quieras
# Muestra el resultado por pantalla
# No modifiques la línea de código

"""
diccionario = {"nombre": "Juan Carlos", "Apellido": "Fernández", "Edad": 28} 

diccionario["Pais"]="España"
print(diccionario)

"""

#19.	Usa un método de tuplas para contar la cantidad de veces que aparece el valor 3 en la siguiente tupla (tupla_ejercicio = (3, 2, 4, 5, 1, 2, 6, 2, 3, 1, 5, 7, 2, 8, 9)) y muestra el resultado en pantalla:

"""
tupla_ejercicio = (3, 2, 4, 5, 1, 2, 6, 2, 3, 1, 5, 7, 2, 8, 9)
lista=list(tupla_ejercicio)
resultado=lista.count(3)

print(resultado)

"""

#20.	Convierte la siguiente tupla (tupla_ejercicio = (1, 2, 3, 4, 5, 1, 2, 3, 4)) en una lista y almacénala en una variable:

"""
tupla_ejercicio = (1, 2, 3, 4, 5, 1, 2, 3, 4)
lista=list(tupla_ejercicio)
print(lista)

"""

#21.	Extrae los elementos de la siguiente tupla(tupla_ejercicio = ("Python", "Java", "PHP", "SQL", "JavaScript", "Django")) en 6 variables a, b, c, d, e, f:

"""
tupla_ejercicio = ("Python", "Java", "PHP", "SQL", "JavaScript", "Django")
a,b,c,d,e,f=tupla_ejercicio
print(f"Los elementos de la tupla son: {a}, {b}, {c}, {d}, {e} y {f}")

"""

#22.	Une los siguientes sets en uno solo:
#{8, 10, "once", "doce"}
#{"once", 4, 5}

"""
set_1={8, 10, "once", "doce"}
set_2={"once", 4, 5}

set_3=set_1.union(set_2)
print(set_3)

"""

#23.	Elimina un elemento al azar del siguiente set(loteria = {"Python", "Java", "SQL", "jQuery", "Git", "Github"}) utilizando métodos adecuados:

"""
loteria = {"Python", "Java", "SQL", "jQuery", "Git", "Github"}
random=loteria.pop()
print(loteria)

"""

#24.	Agrega el nombre de Lorenzo al siguiente set usando métodos adecuados:
#nombres = {"Juan", "Sonia", "Iván", "Mayte", "José Manuel", "Javi", "Miriam"}

"""
nombres = {"Juan", "Sonia", "Iván", "Mayte", "José Manuel", "Javi", "Miriam"}
nombres.add("Lorenzo")
print(nombres)

"""

#25.	Realiza una comparación que tenga como resultado un booleano y almacena el resultado en una variable llamada prueba.

"""
set_1={1,2,"tres"}
set_2={3,"tres"}

prueba=set_1.isdisjoint(set_2)
print(prueba)

"""

#26.	Verifica si 19238 / 38 es mayor que 92*59 y muestra el resultado en pantalla utilizando print. Recuerda que es un booleano.

"""
num_1=19238 / 38
num_2=92*59

print(num_1 >num_2)

"""

#27.	Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado usando print.

"""
num1=25**0.5
num2=5

print(num1==num2)

"""