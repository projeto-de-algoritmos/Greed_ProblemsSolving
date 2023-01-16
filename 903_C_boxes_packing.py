from collections import Counter
 
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
m_c = c.most_common(1)[0][1]
print(m_c)
