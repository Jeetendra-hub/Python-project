#You can check the 41 number of file if you don't understand.
list_of_item = []
no_of_item = int(input("how many item you want to put please enter:"))
for item in range(no_of_item):
    user_chose = input("which type of item you want to put:")
    list_of_item.append(user_chose)
print("OK so can you enter which type of comprehension you want:")
compre = {1: "Set comprehension", 2: "List comprehension",3:"Dictionary comprehension"}
for key, value in compre.items():
    print(f"press {key} for {value}")

user_input=int(input("Enter here:"))
if user_input == 1:
    print("These are item of set comprehension -")
    set={i for i in list_of_item}
    print(set,"\n",type(set))

elif user_input == 2:
    print("You have choose list comprehension")
    lstt=[l for l in list_of_item]
    print(lstt,"\n",type(lstt))

elif user_input == 3:
    print("You have choose dictionary comprehension")
    dict={d:f"input character {d}"for d in list_of_item}
    print(dict,"\n",type(dict))
else:
    print("Invalid input")



# """Comprehenion"""
# lis = []
# n = int(input("How many number you want in list : "))
# for i in range(n):
#     chose = input("Enter any item here: ")
#     lis.append(chose)
#
# u = input("What type of comprehension you want to do (List/Dict/sets : ")
# if u == "List" or u=="list":
#     t = [o for o in lis]
#     print(t)
#
# if u =="Dict" or u == "dict":
#     t = {o:f"item{o}"for o in lis}
#     print(t)
#
# if u == "Sets" or u=="sets":
#     t = {o for o in lis}
#     print(t)



# no_of_list=int(input("How many items add in a list:"))
# input_string=input("Enter a list element seperated by space")
# list=input_string.split()
# t=int(input("Which type of comperhension you use 1. List comp 2.Dictionary comp 3. Set comp"))
# if t ==1:
#     ls = [i for i in list]
#     print(ls)
#     print(type(ls))
# elif t ==2:
#     dict1={f'item{i}':i for i in list}
#     print(dict1)
# elif t ==3:
#     s={i for i in list}
#     print(s)


list_element=[]
number_of_item=int(input("How many item you want ot add?"))
for i in range(number_of_item):
    name_of_item=input("Enter the item name:")
    list_element.append(name_of_item)

print("Thanks now select one of the option:")
option={1:"set comprehension",2:"List comprehension",3:"Dictionary comprehension"}
for key,value in option.items():
    print(f"Press {key} for {value}")

raw_input=int(input("Enter your choice:"))
if raw_input ==1:
    print("Selected for Set comprehension")
    set={i for i in  list_element}
    print(set)
    print(f"type is {type(set)}")














