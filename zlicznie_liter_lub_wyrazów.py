#http://analityk.edu.pl/zliczanie-liter/
iwokacja = "Litwo, Ojczyzno moja! ty jesteś jak zdrowie;Ile cię trzeba cenić, ten tylko się dowie,Kto cię stracił. Dziś piękność twą w całej ozdobieWidzę i opisuję, bo tęsknię po tobie.Panno święta, co Jasnej bronisz CzęstochowyI w Ostrej świecisz Bramie! Ty, co gród zamkowyNowogródzki ochraniasz z jego wiernym ludem!"
poszatkowane = iwokacja.split(" ")
inwo2 = iwokacja.replace('!', '').replace('.', '').replace(',','')
inwo3 = inwo2.replace('.', '')
print("Ilosc liter w tekscie ", len(inwo3))
poszatkowane = inwo2.split(" ")

print(poszatkowane)
print("Ilosc slow: ", len(poszatkowane))
(print(poszatkowane[0].lower))
slownik = {}

#for slowa in poszatkowane:
   # if slowa.lower in slownik:
        #slownik[slowa.lower]+=1
    #else:
        #slownik[slowa.lower]=1
#print(min(slownik, value=slownik.get))            