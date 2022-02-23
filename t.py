# Name: Christian Meier
# Datum: 30.01.2022
# Version: 1.0

# Hardware: LED Strip
#           Real Time Clock

#----- Bibliotheken -----
import machine              # Board   
import neopixel             # Ansteuerung LED´s
from time import sleep      # Wartezeit

#----- Parameter -----
n = 135                     # Anzahl der LED´s
p = 2                       # Ausgang für den Pin

#----- Farben der LED -----
farbe  = (255, 175,  10)    # Weiß
aus    = (000, 000, 000)    # LED´s ausschalten

np = neopixel.NeoPixel(machine.Pin(p), n)

#----- Programm -----
while True:
    for i in range( 0, 10):
        np[i] = farbe
        np.write()
        sleep(1)

    for i in range( 10, 135):
        np[i] = farbe
        np.write()
        sleep(1)

    sleep(180)

    for i in range( 10, n):
        np[i] = aus
        np.write()

    sleep(5)