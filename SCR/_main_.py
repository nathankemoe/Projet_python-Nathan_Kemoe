jouer_1 = input (" pierre'(P)' , feuille'(F)' ou ciseau'(S)' :")
jouer_2 = input (" pierre'(P)' , feuille'(F)' ou ciseau'(S)' :")
print("Jouer 1 a choisi: ", jouer_1)
print("Jouer 2 a choisi: ", jouer_2)
if jouer_1 == "P" and jouer_2 == "F":
    print("Jouer 2 gagne")
elif jouer_1 == "F" and jouer_2 == "S":
    print("Jouer 2 gagne")
elif jouer_1 == "S" and jouer_2 == "P":
    print("Jouer 2 gagne")
elif jouer_1 == jouer_2:
    print("Egalité")
else:
    print("Jouer 1 Gagne")