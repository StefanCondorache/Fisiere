with open('desktop/Lista Clasei 11A.txt', 'r') as f:
    list1=f.readlines()
for i in list1:
    list2=i.split()
    if list2[2]=='engleza' or list2[2]=='Engleza':
        with open('desktop/output1.txt','a') as f:
            x=list2[0]+' '+list2[1]+'\n'
            f.write(x)
    else:
        with open('desktop/output2.txt','a') as f:
            x=list2[0]+' '+list2[1]+'\n'
            f.write(x)
