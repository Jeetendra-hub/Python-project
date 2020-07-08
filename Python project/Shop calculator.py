

sum=0
user=0
while True:
    try:

        user=input("Enter the items price:")

        if user != 'q':

            sum = sum + int(user)

            print("Over all iteams updated:", sum)
        else:
            print("The total amount of bill is:\n",sum)
            break
    except:
        print("Invalid input")

