import os
import sys
import calculation

print "Bienvenue dans Calco qui vous aide a calculer comme jamais !"

x = raw_input("Quel calcul?[A/S/M/D]: ")
#x.upper()

i = raw_input("Selectionner un premier nombre [n1]: ")

y = raw_input("Selectionner un deuxieme nombre [n2]: ")


calc = calculation.calcul()

if x == "A":
    r = int(calc(i, y).addition())
    ar = "addition"
elif x == "S":
    r = calc(i, y).soustraction()
    ar = "soustraction"
elif x == "M":
    calc(i, y)
    r = calc.multiplication()
    ar = "multiplication"
elif x == "D":
    calc(i, y)
    r = calc.division()
    ar = "division"

    print("Pour une "+ ar +", le resultat de "+ str(i) +" et "+ str(y) +"est: "+ str(r))