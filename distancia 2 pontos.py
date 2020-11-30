
           # dAB = math.sqrt(x2 - x1)**2 + (y2-y1)**2

import math

xA = float(input("Primeira coordenada de x: "))
yA = float(input("Primeira Coordenada de y: "))

xB = float(input("Segunda coordenada de x: "))
yB = float(input("Segunda Coordenada de y: "))

dAB = math.sqrt(((xA - xB)**2) + ((yA - yB)**2))

if dAB >= 10:
    print("longe")

else:
    print("perto")
    
