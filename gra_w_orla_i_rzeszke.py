#http://analityk.edu.pl/rzut-moneta-z-python/
import time #Biblioteka czasu, dla wprowadzania opóźnień
import random

def menu():#definiowanie funkcji
    print("##################")
    print("0. Zakończ program")
    print("1. Wybierz Reszkę")
    print("2. Wybierz Orła")
    print("")
def odliczanie():
    print("3!")
    time.sleep(1) #opóźnienie 1s
    print("2!")
    time.sleep(1) #opóźnienie 1s
    print("1!")
    time.sleep(1) #opóźnienie 1s
def wybor_gracza(i):
    if i == 2:
        return "reszka"
    if i == 1:
        return "orzeł"    

x = None
wybor_komputer = None
wynik = {"gracz":0, "komputer":0}
while x!=0:    
    menu() #drukowanie menu z funkcji
    x = int(input("Podaj opcję:")) #należałoby sprawdzić czy wprowadzono cyfrę - by zapobiec błędom
    print("Wprowadzono: ", x)
    odliczanie() #opóźnienie 3 sekundowe
    wybor_komputer = random.choice(["orzeł", "reszka"]) #rejestrowany losowy wybór 
    print("Wypadł(a): ", wybor_komputer)
    print("Wybrano: ", wybor_gracza(x))   
    if wybor_komputer == wybor_gracza(x):
        wynik["gracz"] += 1
        print("Gracz dostaje punkt!")
    else:
        wynik["komputer"] += 1
        print("Komputer dostaje punkt!")
    #1den Reszka, 2 orzeł
    
    print("Wynik: ", wynik)