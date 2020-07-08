
#To calculate the average
'''
n =int(input("Enter the whole list:"))
n=int(n)
average=0
sum=0
for num in range(0,n+1,1):

    sum=sum+num
average=sum/n
print("sum of the first",n,"number is :",average)
'''
#Or we can try this

'''
n=int(input("Enter a number to find the average:"))
a=[]
for i in range(0,n):
    elem=int(input("Enter a element:"))
    a.append(elem)
avg=sum(a)/n
print("Average of element in the list",round(avg,2))
'''

#And we can also try this too

#Average of the number
'''
The average of the number will be first in the from of input of the user and then the variable to keep total
then repeat the function with the for loop and then again the user input for giving each number and then sum it by the
total of the from the user input which will be given by the second time for input number and then find the average of the
number by total / num then print the output. '''


#A simple from of doing the average of a number
'''
num=int(input("Enter any number:"))
total=0
for i in range(num):
    numbers=float(input("Enter the number untill the the above number range end:"))
    total+=numbers
avg=total/num
print("The average of",num,'is here:',avg)
'''


'''
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=int(input("Enter again number:"))

if a>b:
    if a>c:
        print("A is large number:",a)
    else:
        print("C is large number:",c)
else:
    if b>c:
        print("B is large number:",b)
    else:
        print("C is large than all the number:",c)

'''



#Bollean value for (and) operator
'''
your_age=True
your_name=True
if your_age and your_name:
    print("your age is 56 and your name is Reiba")
elif your_name and your_age:
    print("you have mension only name Reiba")
elif not your_name and your_age:
    print("You have mension only age 56")
else:
    print("Noting mension over here")
'''



'''
#  A New input statement for the greater number--
def number_size(num1,num2,num3):

    if num1>num2 and num1>num3:
        print("Big number is:",num1)
    elif num2>num1 and num2>num3:
        print("Big number is:", num2)
    else:
        print("Big number is:", num3)
number_size(input("Enter any number:"),
            input("Enter any number:"),
            input("Enter again number:"))'''





#Finding factrol of a number
'''
def factrol(num):
    if num ==1:
        return num
    else:
        return num*factrol(num-1)
num=int(input("Enter a number:"))
print( factrol(num))'''



#shop calculator
#A while loop
#user item price
#cheak it
#sum it
#repete
#show the total output

'''
sum=0
while True:
    user=input("Enter all the item price:")
    if user!='q':
        sum=sum+int(user)
        print("Over all updata of item price is:",sum)
    else:
        print("User don't want to buy any thing so\n"
              "the total bill is:",sum)
        break
'''

#A leap year program

'''
year=int(input("Enter a year:"))
if year%4==0and year%100!=0 or year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
'''



def factorl(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number*factorl(number-1)

def TrailingZero(number):

    count=0
    i=5
    while number//i != 0:
        count +=int(number/i)
        i=i*5
    return count

if __name__ == '__main__':

    number=int(input("enter a number:"))
    print(TrailingZero(number))
