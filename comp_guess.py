import random

highval=10
lowval=1
ans=0

print "make a number of 1-10 in your mind.."
guess=random.randint(lowval,highval)

print "if I guess:\n \
correct please type \"1\"\n \
larger please type \"2\"\n \
smaller please type \"3\""

while ans!=1:
    print "my guess is :",guess
    ans=input("How's my guess?")
    
    if ans==2:
        lowval=guess+1
    if ans==3:
        highval=guess-1
    guess=random.randint(lowval,highval)
print "finish"
