# Curso básico de Python

En este curso aprenderás a programar en Python.

**Requisitos**
- Python 3,6 o superior instalado
- Computadora con Windows, Linux o MacOS
- Editor de texto como [Visual Studio Code](https://code.visualstudio.com/)

-------------------------
## Primeros pasos en Python: Hola mundo

Como primer paso se programa un "Hola mundo" en Python de modo que este se imprima al ocrrer el programa.

![Hola mundo Python](imagenes\python1.png)

Para correr el programa, junto al triángulo en la parte superior desplegamos el menú de la flecha y presionamos Run Python File

![Run Python File](imagenes\python2.png)

En la terminal se observan los resultados del código, en este caso "Hola mundo!!!!"

![Hola mundo](imagenes\python3.png)

### Concatenaciones

Como primer paso pedimos al usuario un nombre al cual saludaremos.

- Una de las maneras de concatenar dos cadenas es poniendo una "f" antes de la cadena y entre llaves escribir el nombre de la variable.

![Concatenación 1](imagenes\python4.png)

Observamos que el programa pide al usuario su nombre y manda un saludo a este.

![Resultado de concatenación 1](imagenes\python5.png)

- Otra manera de concatenar dos cadenas es escribir una primera cadena y escribir un "+" seguido de la variable a concatenar.

![Concatenación 2](imagenes\python6.png)

Se observa que el programa luego de pedir y recibir el nombre concatena ambas cadenas mandando un saludo.

![Resultado de concatenación 2](imagenes\python7.png)

Los comentarios en el código se agregan con "#".

## Tipos de variables

- STRING o cadena, son caracteres, palabras, texto en general. Todos los valores que se reciben desde el teclado son de este tipo.

![Tipo de variable STRING](imagenes\python8.png)

- ENTERO. Se compone de números sin punto decmial, se usa en operaciones matemáticas y al declararse no se pone el valor entre comillas ya que esto lo convertiría en un STRING.
La diferencia entre un número STRING y uno ENTERO puede observarse durante la suma de sí mismos, ENTERO + ENTERO nos daría como resultado un número resultado de la suma, mientras que STRING + STRING nos daría la concatenación de ambas cadenas.

![Tipo de variable ENTERO](imagenes\python9.png)

Si el valor de las variables es 25 y "25", el resultado de la operación sería 50 para los ENTEROS y 2525 para los STRING.

![Diferencia entre ENTERO y STRING](imagenes\python10.png)

Si se quiere cambiar el tipo de la variable STRING a ENTERO se coloca Variable=int(Variable).

## Condicionales

Si se decea realizar un programa que, dependiendo de los valores que se obtenga, tome decisiones se realiza con "if" seguido de la condición y 2 puntos que simbolizan el inicio del if, lo que se ejecuta en el if debe ser escrito a un espacio de tabulador para que así el progrma entienda lo que es parte de dicha condiciíon. Si se tienen más posibilidades para elegir se puede usar "elif"

![Código condicional](imagenes\python11.png)

FInalmente podemos observar el resultado final del código que de acuerdo a la calificación obtenida y a la edad mandará diferentes mensajes.

![Resultados del cógico condicional](imagenes\python12.png)

## Nota personal:

Importantes los siguientes comando para GitHub:
- git add .
- git commit -m "README añadido"
- git push origin main
- git pull origin main (si algo falla)
