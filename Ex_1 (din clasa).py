with open('desktop/Lista Clasei 11A.txt', 'r') as f:
    list1=f.readlines()
media=0
print('  Nume              Prenume         Nota')
for i,j in enumerate(list1):
    list2=j.split()
    media+=int(list2[2])
    print(i,')',list2[0],(14-len(list2[0]))*' ',list2[1],(14-len(list2[1]))*' ',list2[2])
print('Media clasei a 11A: ',media/len(list1))
