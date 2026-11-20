###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio}, {nom}")

saludar_a("Ivan", "Bon dia")
saludar_a("Maria")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
    return numero%2==0
num = int(input("Introdueix un numero:"))
resultat = es_parell(num)
print(resultat)

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma/len(numeros)

print(mitjana([10,20,30,40,50]))


# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def sumar_tot(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_tot(2,5,10))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
    for i in range(1, limit+1):
        print(f"{i}x{numero}={numero*i}")

taula_multiplicar(3)
taula_multiplicar(1,3)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}:{valor}")

mostrar_perfil(nom="Ivan", edat=19, grau="Marketing i Publicitat")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(n):
    resultat = 1 #APUNTS: fem servir 1 i no 0, perque 0x0=0. 
    comptador = 1
    while comptador<=n:
        resultat *=comptador 
        comptador+=1
    return resultat #APUNTS: tot aixo es per calcular el factorial de un numero. 

def maxim(numeros): #APUNTS: per trobar el numero mes gran de tota la llista.
    valor_maxim = numeros[0]
    
    for numero in numeros:
        if numero > valor_maxim:
            valor_maxim = numero
    
    return valor_maxim 

print(f"El factorial de 5 és {factorial(5)}")  # 120
print(f"El màxim és {maxim([15, 5, 25, 10, 20])}")  # 25

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    comptador = 0
    for lletra in text.lower():
        if lletra in "aeiouàèéíóòïü":
            comptador += 1
    return comptador

print(f"Vocals a 'Hola Caracola': {comptar_vocals('Hola Caracola')}")  # 6


# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
    
    minim = numeros[0]
    maxim = numeros[0]

    for numero in numeros[1:]:
        if numero > maxim:
            maxim = numero
        if numero < minim:
            minim = numero
    return minim, maxim

valor_minim, valor_maxim = minim_i_maxim([1, 6, 90, 100, 3, -4])
print(f"El minim es {valor_minim} i el maxim es {valor_maxim}")
            

# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
def es_palindrom(text):
    text_original = text.lower().replace(" ", "") 
        #APUNTS: el replace serveix per ignorar els espais en blanc quan poses frases. 
    return text_original == text_original[::-1]

print(es_palindrom("Radar"))
print(es_palindrom("aminoacid"))

