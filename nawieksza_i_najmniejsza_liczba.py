#http://analityk.edu.pl/najmniejsza-oraz-najwieksza-liczba-na-liscie-w-python/
lista = [1,3,7,11,2,-6,0]

minimum = None
maximum = None

for element in lista:
    if minimum == None:
        minimum = element
    elif minimum > element:
        minimum = element 

for element in lista:
    if maximum == None:
        maximum = element
    elif maximum < element:
        maximum = element 
                  
print ('Mimimum to: ', minimum)   
print ('Maximum to: ', maximum)    
lista.sort()
print('Posortowana lista: ', lista) 