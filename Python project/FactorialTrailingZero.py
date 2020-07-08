
'''
def factrol(num):
    if num==1:
        return num
    else:
        return num*factrol(num-1)
num=int(input("Enter a number to find the factorl:"))
print(factrol(num))
'''




#part 1
#Another methord of doing the factoral of a number:




def factoral(number):
    if number==0 or number == 1:
        return 1
    else:
        return number*factoral(number-1)


def factorialTrailingZeros(number):
    #fac=factoral(number)
    #print(fac)
    #count=0
    #while fac%10 ==0:
    #count=count+1
    #fac=fac/10
    #return count


    #new from
    count = 0
    i = 5
    # 5!=5*4*3*2*1=120
    # 6!=6*5*4*3*2*1
    ''' so here we wil take the 5 as common because 2 can be divisable by 6,4,2 so we will do the prime factorizaiton
     which will be like 4=2*2 or 6=3*2 which means how many we will get the 5 that much 0 we will get.And 2 is allmost
     menstion in every number
    '''
    while number//i != 0: #Here the number will be divisiable by 5 and not equal to 0
        count+=int(number/i) # we are counting the how many number of 5 are there
        i=i*5 # we will see the how many 25 then how many 125 then how many 625
    return count


if __name__ == '__main__':
    number=int(input("Enter a number:\n"))
    #number=factoral(var)
    #print(f"The factoral of the number is:{fac}")
    print(factorialTrailingZeros(number))


#part - 2

#def factorialTrailingZeros(number):

    #count=0
    #i=5
    # 5!=5*4*3*2*1=120
    # 6!=6*5*4*3*2*1
    ''' so here we wil take the 5 as common because 2 can be divisable by 6,4,2 so we will do the prime factorizaiton
     which will be like 4=2*2 or 6=3*2 which means how many we will get the 5 that much 0 we will get.And 2 is allmost
     menstion in every number
    '''
    #while(number//i != 0): #Here the number will be divisiable by 5 and not equal to 0
        #count+=int(number) # we are counting the how many number of 5 are there
        #i=i*5 # we will see the how many 25 then how many 125 then how many 625
    #return count


#if __name__ == '__main__':
    #var=int(input("Enter a number:\n"))
    #number=int(input("Enter a number:\n"))
    #print(factorialTrailingZeros(number))


#First find the factral of a number
#Then what we will define the function to fine the factral
# we will take care of the 1 and 0 it does'nt make any scence
#Then the factral of a number is what like it is multipleing
#the number by that number then that smaller number then from that smaller number so on to the end of it.

#we have to def a function there
#Next to find the traling zero of a number means we have find first how many zero a number contain so we will count the
#the number as 5 and then divide it with the number and it should not equal to zero. Then we will count how many five are
#there and then at last we will count how many 25 are there how many 125 are there then how many 625 are there so on
#and then it should get a return count ok. then we will give the user input.




