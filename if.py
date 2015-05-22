print "guess from 1-10"
a = 1
b = 7
while a!=b:
    a = input("What's your guess?:")
    if a<b:
        print "larger than that!"
    if a>b:
        print "smaller please!"
print "correct!"
