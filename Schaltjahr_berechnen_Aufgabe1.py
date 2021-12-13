# Name   : Christian Meier
# Klasse : ETS 1
# Datum  : 05.11.2021

prüfJahr = 2100                                                        # Wert einem Namen zugeordnet

if prüfJahr % 4 == 0 and (prüfJahr % 100 !=0 or prüfJahr % 400 ==0):   # %      bedeutet: gebe den Rest einer Ganzzahl aus
    print(prüfJahr ,"ist ein Schaltjahr")                              # ==     bedeutet: ist gleich
                                                                       # !=     bedeutet: ist nicht gleich
else:                                                                  # else   bedeutet: wenn nicht dann
    print(prüfJahr ,"ist kein Schaltjahr")                             # if     bedeutet:   wenn es so ist