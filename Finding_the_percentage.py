n=int(input())
students={}
for i in range(n):
    input1=input().split()
    names=input1[0]
    marks=list(map(float, input1[1:]))
    students[names]= marks
    
nameinput=input()
mark=students.get(nameinput)
if mark:
    average = sum(mark) / len(mark)
    print(f"{average:.2f}")