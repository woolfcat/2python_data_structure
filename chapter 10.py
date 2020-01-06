#重点理解
fh=open('romeo.txt')
counts=dict()
for line in fh:
    line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=list()
for key,val in counts.items():
    newtup=(val,key)
    lst.append(newtup)

lst=sorted(lst,reverse=True)
for val,key in lst[:10]:
    print(key,val)
    
    
#缩略版   
fh=open('romeo.txt')
counts=dict()
for line in fh:
    line.rstrip()
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=sorted([(v,k) for k, v in counts.items()],reverse=True)
for v,k in lst[:10]:
    print(k,v)    
