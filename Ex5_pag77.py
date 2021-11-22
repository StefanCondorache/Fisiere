with open('input.txt','r') as f:
    x=list(f.readline())
j=[i for i in x if i in ['a','o','u','i','e','ă']]
print('numarul de vocale in fisier:',len(j))
