n= int(input())

if (n<10):
    print(n)
else:
    len_n=len(str(n))-1
    p=int('9'*len_n)
    t=n-p
    sum=0
    while(t>0):
        sum+=t%10
        t//=10
    print(sum+9*len_n)
