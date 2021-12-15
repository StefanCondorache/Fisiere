# sa se verifice cate elemente sunt egale cu elementele din colturi
# fisierul si matricea se creeaza automat
import random
x,nr0='',int(input('numarul de randuri si coloane ale unei matrice:'))
with open('desktop/input.txt','a') as f:
    for i in range(nr0):
        for j in range(nr0):
            x+=str(random.randint(0,nr0))+' '
        x+='\n'
        f.write(x)
        x=''
with open('desktop/input.txt','r') as f:
    x=f.readlines()
list1=[]
for i in x:
    list2=i.split()
    list1.append([int(list2[j]) for j in range(len(list2))])
y1,y2,y3,y4=list1[0][0],list1[0][len(list1)-1],list1[len(list1)-1][0],list1[len(list1)-1][len(list1)-1]
nr1,nr2,nr3,nr4=0,0,0,0
for i in list1:
    for j in i:
        if j==y1:
            nr1+=1
        if j==y2:
            nr2+=1
        if j==y3:
            nr3+=1
        if j==y4:
            nr4+=1
print('coltul din dreapta de sus',y1,'se intalneste de',nr1,'ori')
print('coltul din stanga de sus',y2,'se intalneste de',nr2,'ori')
print('coltul din dreapta de jos',y3,'se intalneste de',nr3,'ori')
print('coltul din stanga de jos',y4,'se intalneste de',nr4,'ori')
