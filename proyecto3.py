"""
# Proyecto del tema
Vas a crear un programa que, primero le pida al usuario que ingrese un texto. Puede ser un texto cualquier, como un artículo entero, un párrafo, una frase, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres letras a su elección, y a partir de ese momento nuestro código va a procesar esa información para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1.	¿Cuántas veces aparece cada una de las letras que eligió? Para lograr esto, puedes almacenar esas letras en una lista y luego usar algún método propio de string que permita contar cuántas veces aparece un substring dentro del string. Ten en cuenta que al buscar las letras puede haber mayúsculas y minúsculas, y esto afecta al resultado. Hay métodos que pasan letras a minúsculas o mayúsculas.
2.	Le va a decir al usuario cuántas palabras hay a lo largo de todo el texto. Recuerda que hay un método de string que permite transformarlo en una lista, y que hay funciones que cuentan el largo de una lista.
3.	Va a informar de cuál es la primera letra del texto y cuál es la última.
4.	El sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
5.	El sistema nos va a decir si la palabra “python” se encuentra dentro del texto.

"""

cadena=input("Hola usuario, sea libre de escribir lo que sea y le mostraremos información relevante de lo que ha escrito\nEscriba aquí a continuación: ")

letra_1=input("Ahora, escriba una letra a su elección: ")
letra_2=input("Ahora, otra letra a su elección: ")
letra_3=input("Y finalmente, una tercera: ")

unificador=" "
lista_letras=unificador.join([letra_1,letra_2,letra_3])
lista_letras_minus=lista_letras.lower()
lista_letras=lista_letras_minus.split()

letra_1,letra_2,letra_3=lista_letras

veces_letra_1=cadena.count(letra_1)
veces_letra_2=cadena.count(letra_2)
veces_letra_3=cadena.count(letra_3)

print(f"1)Al parecer has escrito la letra {letra_1} unas {veces_letra_1} vez/veces, mientras que la {letra_2}, ha sido {veces_letra_2} vez/veces, y la {letra_3}, ha sido {veces_letra_3} vez/veces.")


cadena_minus=cadena.lower()



contador_palabras=cadena_minus.split()
print(f"2)Ha escrito un total de {len(contador_palabras)} palabra/palabras")

primera_letra=cadena_minus[0]
ultima_letra=cadena_minus[-1]
print(f"3)La primera letra que ha escrito ha sido la {primera_letra}, mientras que la úlmima es {ultima_letra}")

cadena_reves=cadena[::-1]
print(f"4)Así es como se vería lo que ha escrito si lo hubiera escrito al reves: {cadena_reves}")

existe_python=cadena_minus.find("python")
if existe_python>=0: print("5)Al parecer has escrito Python")
else: print("5)No parece que hayas escrito Python")


