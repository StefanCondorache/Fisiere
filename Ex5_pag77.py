with open('desktop/input.txt','r') as f:
    x=list(f.read())
j=[i for i in x if i in ['a','o','u','i','e','A','O','U','I','E']]
with open('input.txt','a') as f:
    f.write('\n\n')
    for i in j:
        f.write(i+' ')
print('numarul de vocale in fisier:',len(j))
print(*j)
