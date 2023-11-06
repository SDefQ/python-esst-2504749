# Spiel Tic Tac Toe
import os
import random

# Zeichnen des Spielfelds
def zeichneSpielfeld(param_spielfeld):
  print(param_spielfeld[0],'|',param_spielfeld[1],'|',param_spielfeld[2])
  print('---------')
  print(param_spielfeld[3],'|',param_spielfeld[4],'|',param_spielfeld[5])
  print('---------')
  print(param_spielfeld[6],'|',param_spielfeld[7],'|',param_spielfeld[8])

def bildLeeren():
	try:
		os.system("clear")
	except:
		print("Fehler!")

def gewinn_test(param_spielfeld, zeichen):
  if (param_spielfeld[0]==zeichen and param_spielfeld[1]==zeichen and param_spielfeld[2]==zeichen):
    return True
  elif (param_spielfeld[3]==zeichen and param_spielfeld[4]==zeichen and param_spielfeld[5]==zeichen):
    return True
  elif (param_spielfeld[6]==zeichen and param_spielfeld[7]==zeichen and param_spielfeld[8]==zeichen):
    return True
  elif (param_spielfeld[0]==zeichen and param_spielfeld[3]==zeichen and param_spielfeld[6]==zeichen):
    return True
  elif (param_spielfeld[1]==zeichen and param_spielfeld[4]==zeichen and param_spielfeld[7]==zeichen):
    return True
  elif (param_spielfeld[0]==zeichen and param_spielfeld[4]==zeichen and param_spielfeld[8]==zeichen):
    return True
  elif (param_spielfeld[2]==zeichen and param_spielfeld[4]==zeichen and param_spielfeld[6]==zeichen):
    return True
            
      

# Initieren der Spielfeld-Liste
spielfeld = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

my_counter = 0

# Main

zeichneSpielfeld(spielfeld)
while True:
  if (my_counter > 9):
    print("Es steht unentschieden!")
    break

  sp1_wahl = input("Spieler 1 - Wählen Sie ein Feld zwischen 1-9: ")
  spielfeld[int(sp1_wahl)-1]='o'
  my_counter = my_counter + 1
  bildLeeren()
  zeichneSpielfeld(spielfeld)
  if (gewinn_test(spielfeld,'o')):
    print("Spieler 1 hat gewonnen!")
    break

  sp2_wahl = input("Spieler 2 - Wählen Sie ein Feld zwischen 1-9: ")
  spielfeld[int(sp2_wahl)-1]='x'
  my_counter = my_counter + 1
  bildLeeren()
  zeichneSpielfeld(spielfeld)
  if (gewinn_test(spielfeld,'x')):
    print("Spieler 2 hat gewonnen!")
    break
	

	
