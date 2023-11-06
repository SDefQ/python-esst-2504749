def ausgabe_meine_liste(liste):
  for element in liste:
    print("Die Liste enthält das Element:",element)

def meine_mult(parameter1, parameter2):
  return parameter1*(parameter2+2)

def compare3(parameter1, parameter2, parameter3):
  if(parameter1<parameter2) and (parameter2<parameter3):
    return True
  else:
    return False
  
# Test Funktion ausgabe_meine_liste()

test_liste = [0,3,5,12,233]
ausgabe_meine_liste(test_liste)

# Test Funktion meine_mult()

test_param1 = 2
test_param2 = 2
print("Test meine_mult: ",meine_mult(test_param1,test_param2))

# Test Funktion compare3()

var1 = 1
var2 = 3
var3 = 4
var4 = 2

print("1. Test compare: ",compare3(var1,var2,var3))
print("2. Test compare: ",compare3(var1,var2,var4))