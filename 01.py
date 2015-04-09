a = {'A':10,'T':20,'G':5,'C':3,'N':0}
b=a.items()
i=0
while i<len(b):
    if b[i][1]==max(a.values()):
        print b[i][0]
    i+=1
