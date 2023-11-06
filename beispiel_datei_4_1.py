def variablen_ausgabe(parameter):
  print('Die Funktion hat den Parameter',parameter,'bekommen.')

def summe(parameter_a, parameter_b):
  summe = parameter_a + parameter_b
  return summe

mein_parameter = 5

variablen_ausgabe(mein_parameter)

mein_parameter2 = 6

meine_summe = summe(mein_parameter, mein_parameter2)

variablen_ausgabe(meine_summe)