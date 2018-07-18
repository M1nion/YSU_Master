E0 = 100
Emax = 100
bisvalue = 50
bis_exp = 40
EC50 = 4.700
r = 3

cefinal = ((E0-bisvalue)/Emax*(EC50**r)/(1-(E0-bisvalue)/Emax))**(1.00/r)

CE = float('%.2f' % cefinal)
print(CE)