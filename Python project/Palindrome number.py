

#what is parlindrome number?
#The reverse of a given number is equal to the same number.

num=int(input("Enter a number:"))
temp=num
sum=0

while(num>0):
    remider=num%10
    sum=sum*10+remider
    num=num//10

if temp==sum:
    print(sum,"is palindrome number")

else:
    print(sum,"is not palindrome number")

#Or we can write this
num=int(input("Enter a number:"))
temp=num
sum=0
while(temp>0):
    sum=sum*10+(temp%10)
    temp=temp//10
if num==sum:
    print("Its a palindrome number")
else:
    print("Its not a palindrome number")













