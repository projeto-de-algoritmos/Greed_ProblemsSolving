n, m = map(int, input().split())

rep=True
s=0

input_matrix = []
for i in range(n):
	input_matrix.append(list(map(int,input().split())))

for k in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        cur = input_matrix[k][j]
        if not cur:
            mi = min(input_matrix[k+1][j]-1,input_matrix[k][j+1]-1)
            input_matrix[k][j] = mi 
            cur = mi
            s += mi
        if k < n-1 and input_matrix[k+1][j]: 
            if cur>=input_matrix[k+1][j]: 
                rep = False;
        if j < m-1 and input_matrix[k][j+1]: 
            if cur>=input_matrix[k][j+1]: 
                rep = False;
        if k > 0 and input_matrix[k-1][j]:
            if cur<=input_matrix[k-1][j]: 
                rep = False;
        if j > 0 and input_matrix[k][j-1]:
            if cur<=input_matrix[k][j-1]: 
                rep = False;

if rep: 
    print(sum([sum(e) for e in input_matrix]))
else: 
    print(-1)
