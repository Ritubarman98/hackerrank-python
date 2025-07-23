s=[]
n=[]
n_list=[]
for i in range(int(input())):
    name=input()
    score=float(input())
    s.append(score)
    n.append([name,score])
#print(s)
#print(n)
y=sorted(list(set(s)))
#print(y)
#print(y[1])
for name, score in n:
    if score==y[1]:
        n_list.append(name)
#print(n_list)
n_list.sort()
for item in n_list:
    print(item)
