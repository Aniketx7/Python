# Types of function argument in python
""" 1> Default argument    --A default value given to argument
 2> keyword argument    --you can call function in any order
 3> required argument   --required means required ( you have to give a value while calling function )
 4> variable length argument    --helps in pass more argument than those defined in the actual function.
"""

# Default argument       A default value given to argument


def average(a=5, b=9):
    print("average of ", a, "&", b, "is", (a + b) / 2)


average(3, 5)
average()  # here average will show of 5 and 9

average(3)  #   now value of a is 3
average(b=4)  # now value of b is 4 and of a is 5

print("")
print("****************")


# keyword argument
def name(fname, lname):
    print("hello", fname, lname)


name("kumar", "aniket")
name(lname="Kumar", fname="Aniket")  # here order doesn't matter

print("")
print("****************")


# required keyword
def mean(a, b=1):  # now a is required keyword, you have to given value of it
    print("mean  of ", a, "&", b, "is", (a + b) / 2)


mean(5)

print("")
print("****************")


# Variable length argument
"""sometimes we need to pass more argument than those defined in the actual function. This can be done through variable length argument  
    To ways to achieve this:
        i> Arbitary argument    -- pass a '*' before the parameter name while defining a function. The function accesses the argument by processing them in the form of tuple

        example: """

def car(*name):
    print(name[0], name[2])         #shows 0's and 2nd value 
    print(name)             #shows all value of argument

car('BMW', 'Rolls Royce ', 'Bugatti')           #output: BMW, Bugatti

print("")
print("****************") 

def average(*num):
    sum = 0
    for i in num:   
        sum += i
    print('sum=', sum, 'len of num=', len(num), 'average=', sum/len(num))           #This is outside of for loop 


average(3, 5, 2, 5, 3)


    # second ways of variable length argument
#Keyword Arbitary Arguments     -- pass a '**' beofore the parameter name while defining the function. The function access the argument by processing them in the form of dictionary            Example

def fullname(**name):
    print('Hii', name['fname'], name['lname'])

fullname(fname = 'Aniket', lname='Kumar')



#return statement
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))