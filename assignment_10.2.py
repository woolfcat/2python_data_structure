'''
10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
'''

.....answer.....

fh=open('mbox-short.txt')
hc=dict()
for li in fh:
    if li.startswith('From'):
        li.rstrip()
        wds=li.split()
        if wds[0]!='From':
            continue
        tm=wds[5].split(':') 
        hc[tm[0]]=hc.get(tm[0],0)+1
        

for h,t in sorted(hc.items()):
    print(h,t)







.....Processing.....

fh=open('mbox-short.txt')
hc=dict()
for li in fh:
    if li.startswith('From'):
        li.rstrip()
        wds=li.split()
        if wds[0]!='From':
            continue
        print(wds)
        print(wds[5])
        tm=wds[5].split(':')
        print(tm)
        print(tm[0])
        hc[tm[0]]=hc.get(tm[0],0)+1
        print(hc)
print(hc)
print(hc.keys())

for i in sorted(hc.items()):
    print(i)

for h,t in sorted(hc.items()):
    print(h,t)

    
....6/1/2020....
fh=open('mbox-short.txt')
hc=dict()
for line in fh:
    if line.startswith('From'):
        li=line.rstrip()
        l=li.split()
        if l[0]!='From':
            continue
        ti=l[5].split(':')[0]
        hc[ti]=hc.get(ti,0)+1
        
for h,c in sorted(hc.items()):
    print(h,c)
