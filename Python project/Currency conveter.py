'''
#opening a file named currencydata.txt
with open("currencydata.txt") as d:
    lines=d.readlines()


currencydic={}
anotherlist={}
for line in lines:
    parsed=line.split("\t")
    currencydic[parsed[0]]=parsed[1]
    anotherlist[parsed[0]]=parsed[1]=parsed[2]


amount=int(input("Enter the amount:\n"))
print("Choose one of the currency from the list given below ? Available options:\n")
[print(item) for item in currencydic.keys()]
currency=input("Please enter one of these value:\n")
print(f"{amount} INR is equal to {amount*float(currencydic[currency])} {currency}" )
print(f"And the amount to convert in indian rupees is:{amount*float(anotherlist[currency])} rupees")

'''

#practicing that thing only


#To read a file we are in the writing the with function and then we are opening the file with the name of file as d is a
# d is variable -- which will strore in d and then in the next line we are giving the new variable and reading the line
# which is we can write the lines=d.readlines()--> is also a function ok.

with open("currencydata.txt") as d:
    lines=d.readlines()
'''
At first we are using the for loop and giving the line which is the variable line in lines and lines is what we are
mensioning in the at the top which we are reading the file and all that reading file is store in this lines variable.
Then comming to do split which is also store in a new varable which can be look like fasred=line.split(\t) Here line is
the variable which is in the for loop.And split help to divide data. And then we are creating the dictonary address
 which is currencydic[fasred[0]]=fasred[1] so we have to menstion the address to get two value country name and the
 currency.
'''

currencydic={}
for line in lines:
    fasred=line.split("\t")
    currencydic[fasred[0]]=fasred[1]

#Then amount is for input the data and then we are printing what will show after then input so we print the data of
#choose one of the option you want to see the changes of currency and then first we are making the list and in that
#list we are writing the print(text) here text is the variable that is mension in the for loop and then we will write
#the for loop which will be the variabel text and that will remain in the dictonary and the improtant the keys so we are
#writing the keys like this [print (text) for text in currencydic.keys()] .
#And then creating the input form to put the currency name to determine the list of the country.
#And then we are creating the print to get the result of the statement and to form the output
#AS it look like this -->print(f"{amount}INR is equal to {amount*float(currecydic[currency])}{currency}")

#Here the amount is the variable which we have mension at the top and it should get a curly brace

try:
    amount=int(input("Enter a number:\n"))
    print("Choose one of the option you want to see the changes of currency:\n")
    [print(text) for text in currencydic.keys()]
    currency=input("Enter the name of the give list:\n")
    print(f"{amount} INR is equal to {amount*float(currencydic[currency])} {currency}")
except:
    print("something went wrong please make sure its correct or not...")



#Practic part

'''
with open("currencydata.txt") as d:
    lines=d.readlines()

currencydic={}
for line in lines:
    phared=line.split("\t")
    currencydic[phared[0]]=phared[1]

amount=int(input("Enter the amount:\n"))
print("Select one of the curreceny that you want to see the value(Given below):\n")
[print(text) for text in currencydic.keys()]
currency=input("Enter what type of currency you want:\n")
print(f"{amount} INR is equal to {amount*float(currencydic[currency])} {currency}")

'''





