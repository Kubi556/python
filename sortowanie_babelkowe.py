#http://analityk.edu.pl/sortowanie-babelkowe/
A = [4,11,12,16,19,36,2,9,35,-2,-6,-8,-1,-39,1,5,3,6,0]
#max2 = 0
#min2 = 0
print('dlugosc A: ', len(A))
zmiany=None

while zmiany!=0:
    zmiany = 0 
    for i in range(0,len(A)-1):
        if A[i] > A[i+1]:
            zmiany += 1 
            #print(iteracje, " - numer iteracji")
            A[i], A[i+1] = A[i+1], A[i]
print(A)    
