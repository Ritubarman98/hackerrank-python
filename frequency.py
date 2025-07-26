s=input()
s=s.lower()
arr=[]
s1={}
for i in range(len(s)):
    if s[i].isdigit() or s[i].isalpha():
        arr.append(s[i])
arr.sort()
#print(arr)
for i in (arr):
    if i in s1:
        s1[i] +=1
    else:
        s1[i] = 1
#print(s1)
for i in (s1.keys()):
    print(i, ":" , s1[i])