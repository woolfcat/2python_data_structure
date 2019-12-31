'''
9.4 Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop
to find the most prolific committer.
'''

fh=open('mbox-short.txt')
em=dict()
for l in fh:
    if l.startswith('From'):
        l.rstrip()
        m=l.split()
        if not m[0]=='From':
            continue
        em[m[1]]=em.get(m[1],0)+1
print(em)

ge=None
gt=None
for e,t in em.items():
    if gt==None or gt<t:
        gt=t
        ge=e
print('the most prolific committer is',ge,'with',gt,'times')
