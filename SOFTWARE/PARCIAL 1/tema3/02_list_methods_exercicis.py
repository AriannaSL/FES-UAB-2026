###
# EXERCICIS
# Fes servir, sempre que puguis, els mètodes que has après.
###

# Exercici 1: Afegir i modificar elements
# Crea una llista amb els nombres de l'1 al 5.
llista = [1, 2, 3, 4, 5]
# Afegeix-hi el nombre 6 al final fent servir append().
llista.append(6)
# Insereix-hi el nombre 10 a la posició 2 fent servir insert().
llista.insert(2,10)
# Modifica el primer element de la llista perquè sigui 0.
llista[0]=0
print(llista)


# Exercici 2: Combinar i buidar llistes
# Crea dues llistes:
llista_a = [1, 2, 3]
llista_b = [4, 5, 6, 1, 2]
# Amplia llista_a amb llista_b fent servir extend().
llista_a.extend(llista_b)
# Elimina la primera aparició del nombre 1 de llista_a fent servir remove().
llista_a.remove(1)
# Elimina l'element de l'índex 3 de llista_a fent servir pop(). Imprimeix l'element eliminat.
element_eliminat = llista_a.pop(3)
print(element_eliminat)
# Buida completament llista_b fent servir clear().
llista_b.clear()
print(f"Llista a: {llista_a}")
print(f"Llista b: {llista_b}")



# Exercici 3: Slicing i eliminació amb del
# Crea una llista amb els nombres de l'1 al 10.
llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Fes servir slicing i del per eliminar els elements des de l'índex 2 fins al 5
# (sense incloure el 5).
del llista[2:5]
# Imprimeix la llista resultant.
print(llista)


# Exercici 4: Ordenar i comptar
# Crea una llista amb els nombres següents: [5, 2, 8, 1, 9, 4, 2].
llista = [5, 2, 8, 1, 9, 4, 2]
# Ordena la llista de manera ascendent fent servir sort().
llista.sort()
print(llista)
# Compta quantes vegades apareix el nombre 2 a la llista fent servir count().
comptador_dos = llista.count(2)
print(comptador_dos)
# Comprova si el nombre 7 és a la llista fent servir in.
comprova_set = 7 in llista
print(comprova_set)


# Exercici 5: Còpia i referència
# Crea una llista anomenada original amb els nombres [1, 2, 3].
original = [1, 2, 3]
print(original) 
    # --> depen d'on el posis et donara [1,2,3] o [10,2,3]
# Crea'n una còpia anomenada copia_1 fent servir slicing.
copia_1 = original[:]
# Crea'n una altra còpia anomenada copia_2 fent servir copy().
copia_2 = original.copy()
# Crea una referència a la llista original anomenada referencia.
referencia = original
# Modifica a 10 el primer element de la llista referencia.
referencia [0] = 10
# Imprimeix les quatre llistes (original, copia_1, copia_2 i referencia) i observa'n els canvis.

print(copia_1)
print(copia_2)
print(referencia)

# Exercici 6: Ordenar cadenes sense distingir entre majúscules i minúscules
# Crea una llista amb les cadenes següents: ["Poma", "pera", "PLÀTAN", "taronja"].
llista = ["Poma", "pera", "PLÀTAN", "taronja"]
# Ordena la llista sense distingir entre majúscules i minúscules.
llista.sort(key=str.lower)
print(llista)
