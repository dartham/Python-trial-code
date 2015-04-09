#function
def top_buttom(size):
    line=''
    for i in range(size):
        line += '*'
    print line

def body(size):
    star= '*'
    space=''
    for i in range(size-2):
        space += ' '
    print star+space+star
    
def square_box(size):
    top_buttom(size)
    for i in range(size-2):
        body(size)  
    top_buttom(size)

############################################################################

#variables    
size=0
upper=40
lower=5
max_error=3
error_count=0

#main
while (not(lower<=size<=upper)) and error_count<max_error:
    size = input("Enter size:")
    if (not(lower<=size<=upper)) and error_count<max_error:
        print "Please enter number in the avaliable range of 5-40"
        error_count += 1
 
if error_count<max_error:
    square_box(size)
else:
    print "you enter too much of errors... goodbye"
