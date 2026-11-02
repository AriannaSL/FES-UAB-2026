###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom, xarxa = input("Introdueix el nom d'un tecnic i el nom de la xarxa que està instal·lant separats per una coma: ").split(",")
print(f'El nom del tecnic es {nom} i el de la xarxa es {xarxa}')

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud = float(input("Quina es la longitud d'un enllaç de fibra en km: "))
velocitat = float(input("Quina es la velocitat de transmissió: "))
segons = 8/velocitat
print(f"Necessitaries {segons} segons per transmetre 1GB a traves de {longitud} km d'enllaç")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_feina = float(input("Nombre d'hores de feina: "))
preu_hora = float(input("Preu per hora d'una instal·lacio de xarxa: "))
preu_material = float(input("Preu material: "))
total = (preu_hora * hores_feina) + preu_material
print(f"Cost total de la instal·lacio: {total}")
