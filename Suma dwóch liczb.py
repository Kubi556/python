#http://analityk.edu.pl/suma-dwoch-liczb/
S = [1,3,5,2,11,7]
    #0,1,2,3, 4,5] - indeksy listy
suma9 = False #fałsz
print('Długość S to : ', len(S))
print(S[len(S)-2])
for i in range(0, len(S)-1): #największe i powinno być przedostatnim elementem na liście
    #i = 0 - pierwsza iteracja
    #i = 1 - druga iteracja tej pętli
    for j in range(i+1, len(S)):
        #i=0, j=0 - 1wsza iteracja 
        #i=0, j=1 - 2ga iteracja
        print("Pary liczb użyte: ", S[i], ', ', S[j])
        if S[i] + S[j] == 9:
            print("Znalazłem elementy których suma to 9! Są to: ", S[i], " oraz ", S[j] )
            suma9 = True #prawda
print("Czy któreś dwie liczby dają sumę 9? : ", suma9)