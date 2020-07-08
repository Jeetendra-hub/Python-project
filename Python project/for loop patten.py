'''
#printing the * patten in for range function
for r in range(5):
    for c in range(r+1):
        print("* ",end='') #end is a parameter denoting to keep all the string in a range of sequence like (********) this.
                            #And we know that new line in bydefault locate in python.

    print("\r") # \r is for escapeing all the previous string and display the rest of the remain string.
            #Or search by google is that \r is a regular expression that matches an empty line. The \r is a raw string
            #escape sequence not parsed.For expample \n


#print a number pattern using a for loop
num1=input("Enter a number:")
num1=int(num1)
for r in range(num1):
    for c in range(r+1):
        print(r,end=" ")
    print("\r")


#Triangular half pyramid number pattern
num2=int(input("Enter a numeber:"))
for r in range(num2):
    for c in range(r+1):
        print(c,end=" ")
    print("\r")



#Third number pattern
num3=int(input("Enter a number:"))
for r in range(1,num3):
    for c in range(r,0,-1):
        print(c,end=" ")
    print("\n")


#Forth number pattern
print("Forth number pattern")
last_number=12
for i in range(last_number):
    for j in range (-1+i,-1,-1):
        print(format(2**j, "4d"),end=" ")
    print(" ")


#Fifth number pattern
print("Fifth number pattern")
last_number=9
for i in range(1,last_number):
    for i in range(0,i,1):
        print(format(2**i,"4d"),end=' ')
        for i in range(-1+i,-1,-1):
            print(format(2**i,"4d"),end=" ")
        print("\r")
'''

'''
print("Number pattern ex-7")
start=1
stop=2
currentNumber=stop
for row in range(2,6):
    for col in range(start,stop):
        currentNumber-=1
        print(currentNumber,end=" ")
    print(" ")

    start=stop
    stop+=row
    currentNumber= stop



#PRINTING FULL TRIANGLE PYRAMID USING STARS

size=7
m=(2*size)-2
for i in range(0,size):
    for j in range(0,m):
        print(end=" ")
    m=m-1 #decrementing m after each loop
    for j in range(0,i+1):
        #printing full Triangle pyramid using stars
        print("*",end=" ")
    print("\r")


#Program to print inverted half pyramid using an Asterisk(star)
print("\nProgram to print half pyramid:")
rows=input("Enter number of rows")
rows=int(rows)
for i in range(rows,0,-1):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
'''
#print Asterisk (start) pattern
print("Program to print start pattern:\n")

rows=input("Enter max star to be diplay on single line:")
rows=int(rows)
for i in range(0,rows):
    for j in range (0,i+1):
        print("*",end=" ")
    print("\r")
for i in range(rows,0,-1):
    for j in range(0,i,-1):
        print("*",end=' ')
    print("\r")


#print an inverted half pyramid pattern using a number
rows=5
for i in range(rows,0,-1):
    for j in range(0,i+1):
        print(j,end=" ")
    print("\r")


print("Print Alphabets and letters pattern in python")
lastNumber=6
asciiNumber=65
for i in range(0,lastNumber):
    for j in range(0,i+1):
        character=chr(asciiNumber)
        print(character,end=" ")
        asciiNumber+=1
    print(" ")


#Heat shape in python
print("\n")
for rows in range(6):
    for cols in range(7):
        if(rows==0 and cols%3!=0)or (rows==1 and cols%3==0) or (rows-cols==2) or (rows+cols==8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#Explain in notepad (For loop heart pattern) saved



