###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí
nom= "Arianna"
ciutat= "Barcelona"
print(nom)
print(ciutat)

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

### Completa aquí

print("tipus de a: ", type(a))
print("tipus de b: ", type(b))
print("tipus de c: ", type(c))
print("tipus de d: ", type(d))
print("tipus de e: ", type(e))


print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí

cadena= "12345"
enter= int(cadena)
decimal=float(enter)

print("Nombre enter: ", enter)
print("Nombre decimal: ", decimal)

decimal2= 3.99
enter2= int(decimal2)
print("Conversió de float 3.99 a enter: ", enter2)


print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 40 anys i faig 1.75 metres"
#name = "Marc"
#age = 40

### Completa aquí´

nom="Arianna"
edat=19
alçada=1.58

print(f"Hola! Em dic {nom}, tinc {edat} anys i faig {alçada} metres")
# la f es per mostrar la presentació amb una f-string

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

resultat= int(round(3.1416)/2) #arrodonim directament PI sense desar-lo en una variable. 
print("Valor PI:", 3.1416)
print("PI arrodonit:", round(3.1416))
print("El resultat hauria de ser:", resultat)

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí
celsius = float(input("Introdueix la temperatura en ºC:"))
Fah = (celsius*9/5)+32
print(f"Els {celsius} es converteixen en {Fah:.2f} ºF")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí
total = float(input("El total del compte es:"))
p_propina = float(input ("El percentatge de propina es:"))

propina = total * (p_propina/100)
total_final = total + propina
print(f"Propina: {propina:.2f}")
print(f"Total a pagar: {total_final:.2f}")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí

contrasenya = input("Contrasenya:")
if len(contrasenya)< 8:
    print("Contrasenya no valida")
else:
    print("Contrasenya valida")