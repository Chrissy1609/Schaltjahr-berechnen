# Name   : Christian Meier
# Klasse : ETS 1
# Datum  : 05.11.2021

Jahre =[]                                                                           # Liste die Ausgegeben wird

minJahr = 1799                                                                      # Start der Liste
maxJahr = 2301                                                                      # Ende  der Liste
for i in range(maxJahr - minJahr):                                                  # Anzahl der Durchgänge der Schleife
    pruefJahr = minJahr + i                                                         # Das Jahr das überprüft wird
    if (pruefJahr % 4 ==0 and (pruefJahr % 100 != 0 or pruefJahr % 400 ==0)):       # % bedeute den Rest der Ganzzahl ausgeben
        Jahre.append(pruefJahr)                                                     # == bedeutet ist gleich / != bedeutet ist nicht gleich
                                                                                    # (Jahre) = Liste / .append = etwas zur Liste hinzufügen
    print(Jahre)                                                                    # Liste Jahre ausgeben