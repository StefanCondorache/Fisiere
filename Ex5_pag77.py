with open('input.txt','r') as f:
    x=list(f.readline())
j=0
for i in x:
    if i in ['a','o','u','i','e','ă']:
        j+=1
print('numarul de vocale in fisier:',j)