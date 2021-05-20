l = []
while(True):
    n=int(input())
    if(n>0):
        l.append(n)
    else:
        break

minv = l[1]
maxv = l[1]
i = 0
while i<len(l):
    if(maxv < l[i]):
        maxv = l[i]
    if(minv > l[i]):
        minv = l[i]
    i += 1
print(minv,maxv)
