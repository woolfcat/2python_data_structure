'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the
line into a list of words using the split() method. The program should build a
list of words. For each word on each line check to see if the word is already
in the list and if not append it to the list. When the program completes,
sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''
METHOD-1：

fname=input("enter the file name:")
fh=open(fname)
words=list()

for line in fh:
    line=line.rstrip(' ')
    l=line.split()
    for word in l:
        if word not in words:
            words.append(word)
            
words.sort()
print(words)




METHOD-2：

fh=open('romeo.txt')
words=list()

for line in fh:
    line=line.rstrip(' ')
    l=line.split()
    words=words+l

s=set(words)
words=list(s)
            
words.sort()
print(words)
