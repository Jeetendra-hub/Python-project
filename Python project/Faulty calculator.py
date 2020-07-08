

# Here we want a faulty calculator which will show the worng result and it will just print that result like ex-45*3=real is
#135 but in faluly the conditon is given for to do this 45*3=555 so we are printing it as well.

while True:
    print("\n\nWELCOME TO MY CALCULATOR\t DEVELOPED BY-DEEPENDRA KUMAR ROUT\n")
    print("Press ( + ) for addition")
    print("Press ( - ) for subtraction")
    print("Press ( * ) for multiplication")
    print("Press ( % ) for reminder")
    print("Press ( // ) for floor value")
    print("Press ( ** ) for power value")
    print("Press ( / ) for division\n\n")


    opr=input("choose one of the above operator:")
    num1=int(input("\nEnter the 1st number:"))
    num2 = int(input("Enter the 2nd number:"))

    if opr=='+':
        if(num1==56):
            print("56+9=77")
        else:
            print(f"\nFOR ADDITION YOUR RESULT : {num1}+{num2}={num1+num2}")
    elif (opr == "-"):
            print(f"\nFOR SUBTRACTION YOUR RESULT : ,{num1} -{num2}={num1-num2}")
    elif (opr == "*"):
        if(num1==45):
            print("45*3=555")
        else:
            print(f"\nFOR MULTIPLICATION YOUR RESULT : {num1} * {num2} = {num1 * num2} ")
    elif(opr=="/"):
        if(num1==56):
            print("56/4")
        else:
            print(f"\nFOR DIVISION YOUR RESULT : {num1} / {num2} = {num1 / num2} ")
    elif(opr=="%"):
        print(f"\nFOR REMINDER VALUE YOUR RESULT : {num1} % {num2} = {num1 % num2} ")
    elif(opr=="//"):
        print(f"\nFOR FLOOR YOUR RESULT : {num1} // {num2} = {num1 // num2} ")
    elif(opr=="**"):
        print(f"\nFOR POWER OF A NUMBER YOUR RESULT : {num1} ** {num2} = {num1 ** num2} ")
    else:
        print("\nINVALID INPUT>>><<<")
    restart =str(input("\n\nDo you want to restart press [Y for yes] / [N for NO] :"))
    if restart  == "Y".lower():
        continue
    elif restart =="N".lower():
        print("USER WANT TO QUIT")
        break

