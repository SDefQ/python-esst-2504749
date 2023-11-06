# Kleines Spiel gegen den Computer
# Das Spiel heißt Schere, Stein oder Papier.

import random

# Gewinnbedingung: Schere verliegt gegen Stein. Stein verliert gegen Papier. Papier verliert gegen Schere.

def userwahl_mapping(var_user):
  if ((var_user=="Schere") or (var_user=="schere")):
    return 0
  elif ((var_user=="Stein") or (var_user=="stein")):
    return 1
  elif ((var_user=="Papier") or (var_user=="papier")):
    return 2
  else:
    return 3
  
def wer_gewinnt(var_user, var_computer):
  if ((var_user==0) and (var_computer==0)):
    print("Unentschieden, der Computer und Sie haben Schere gewählt.")
  elif ((var_user==1) and (var_computer==1)):
    print("Unentschieden, der Computer und Sie haben Stein gewählt.")
  elif ((var_user==2) and (var_computer==2)):
    print("Untentschieden, der Computer und Sie haben Papier gewählt.")
  elif ((var_user>=3)):
    print("Es tut mir leid, aber Sie haben eine ungültige Wahl getroffen.")
  elif ((var_user==0) and (var_computer==1)):
    print("Verloren, Stein macht Schere stumpf!")
  elif ((var_user==0) and (var_computer==2)):
    print("Gewonnen, Schere schneidet Papier!")
  elif ((var_user==1) and (var_computer==0)):
    print("Gewonnen, Stein macht Schere stumpf!")
  elif ((var_user==1) and (var_computer==2)):
    print("Verloren, Papier umwickelt den Stein!")
  elif ((var_user==2) and (var_computer==0)):
    print("Verloren, Papier wird von Schere zerschnitten!")
  elif ((var_user==2) and (var_computer==1)):
    print("Gewonnen, Papier umwickelt den Stein!")
  else:
    print("Es gab eine von beiden Seiten ungültige Wahl!")

beenden = ''
userwahl = ''

print("Spielen wir Schere, Stein, Papier.")
print("Sie fangen an. Wenn Sie nicht mehr wollen, dann können sie das Spiel mit Q beenden.")
print("")

while (beenden != 'Q'):
  userwahl = input("Wählen Sie Schere, Stein oder Papier: ")
  print("Sie haben", userwahl,"gewählt.")
  userwahl_zahl = userwahl_mapping(userwahl)

  computerwahl_zahl = random.randint(0,2)
  print("Der Computer hat",computerwahl_zahl,"gewählt.")

  wer_gewinnt(userwahl_zahl, computerwahl_zahl)

  print("")
  beenden = input("Wollen Sie das Spiel beenden, dann tippen Sie Q. ")

