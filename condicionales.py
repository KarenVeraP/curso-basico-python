# Declaramos una variable
calificacion = input("Introduce tu calificación de la AZ-9000: ")

calificacion = int(calificacion)

# Preguntamos si la calificaciín es menor a 700
if calificacion < 700 :
    print("Veees?, por no estudiar") # Si es menor a 700, muestra esto
elif calificacion > 1000 :
    print("Mientes!!!!! No puedes sacar más de 1000")
else : # Si no se cumple el if anterior, pasa a esta línea
    print("Felicidades, pasa por tu certificaado") # Se ejecuta si ninguno de los if se cumple

# Verificador de mayoría de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")