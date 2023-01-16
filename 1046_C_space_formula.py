n, d=map(int,input().split())
s=list(map(int,input().split()))
p=list(map(int,input().split()))

s[d-1]+=p[0]
p.reverse()
l=[]

for i in range(d):
    if s[i]<=s[d-1]:
        idx=i
        break

curr=0
i=idx

while i<d-1:
    if s[i]+p[curr]<=s[d-1]:
        l.append(i)
        curr+=1
        i+=1
    else:
        if len(l)>0:
            l.pop(0)
            curr-=1
        else:
            i+=1
print(d-len(l))
