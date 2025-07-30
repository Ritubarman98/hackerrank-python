p, q, r=map(int, input().split())
matrix1=[]
matrix2=[]

for i in range(p):
    rows1=list(map(int, input().split()))
    matrix1.append(rows1)

for i in range(q):
    rows2=list(map(int, input().split()))
    matrix2.append(rows2)
#print(matrix1)
#print(matrix2)

result = []
for i in range(p):
    row = []
    for j in range(r):
        row.append(0)
    result.append(row)
#print(result)

for i in range(p):
    for j in range(r):
        for k in range(q):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
for i in result:
    print(*i)
            