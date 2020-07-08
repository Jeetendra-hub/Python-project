def factorl(number):
    if number ==0 or number ==1:
        return 1
    else:
        return number*factorl(number-1)



def FactoialTrailingZero(number):
    count = 0
    i = 5
    # 5!=5*4*3*2*1=120
    # 6!=6*5*4*3*2*1
    #100!=100//5 + 100/5*5
    ''' so here we wil take the 5 as common because 2 can be divisable by 6,4,2 so we will do the prime factorizaiton
     which will look like this 4=2*2 or 6=3*2 which means how many we will get the 5 that much 0 we will get.And 2 is allmost
     menstion in every number
    '''
    while number // i != 0:  # Here the number will be divisiable by 5 and not equal to 0
        count += int(number / i)  # we are counting the how many number of 5 are there
        i = i * 5  # we will see the how many 25 then how many 125 then how many 625
    return count


if __name__ == '__main__':
    number=int(input("Enter a number:"))
    print(FactoialTrailingZero(number))

