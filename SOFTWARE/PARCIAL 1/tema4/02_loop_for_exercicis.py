###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
print("\n Exercici 1:")
for numero in range(2,21,2): #range(inici, final, pas)
    print(numero)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
print("\n Exercici 2:")
numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
suma = 0
for numero in numeros:
    suma+= numero
mitjana = suma/len(numeros)
print(f"La mitjana es: {mitjana}")

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
print("\n Exercici 1:")
numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
maxim = numeros[0]
for numero in numeros:
    if numero > maxim:
        maxim = numero
print(f"El numero maxim de la llista es: {maxim}")

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
print("\n Exercici 4:")
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
paraules_cinc_lletres = [paraula for paraula in paraules if len(paraula) > 5]
print(paraules_cinc_lletres)

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
print("\n Exercici 5:")
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
lletra = input ("Introdueix una lletra: ").lower()
comptador = 0
for paraula in paraules:
    if paraula.lower().startswith(lletra):
        comptador += 1
print(f"A la llista hi ha {comptador} paraules que comencen per la lletra {lletra}")

# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
print("\n Exercici 6:")
tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.
suma = 0
for tensio in tensions:
    suma += tensio
mitjana = suma/len(tensions)
print(f"La mitjana de tensions es: {mitjana}")

# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
print("\n Exercici 7:")
resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.
suma = 0
for resistencia in resistencies:
    corrent = 12/resistencia
    print(f"El corrent que circula per {resistencia} Ω, es de {corrent:.4f} A")

# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
print("\n Exercici 8:")
nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.
mostres = 0
for nivell_soroll in nivells_soroll:
    if nivell_soroll > -80:
        mostres += 1
print(f"Hi han {mostres} que superen els -80dBm")


# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
print("\n Exercici 9:")
bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).
diferents = 0
for i in range(len(bits_transmesos)):
    if bits_transmesos[i] != bits_rebuts[i]:
        diferents += 1

taxa = diferents/len(bits_transmesos)

print(f"Hi ha {diferents} bits diferents.")
print(f"La taxa d'error es de {taxa}")



# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
print("\n Exercici 10:")
frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.
for frequencia in frequencies:
    periode = 1/frequencia
    print(f"El periode de {frequencia}Hz es {periode}s")