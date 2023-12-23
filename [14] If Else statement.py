"""'Types of conditional statement
1> if-else
2> elif
3> nested-if statement"""

# Tab spaces below if statement is necessary        to Execute as conditional statement (otherwise )

budget = 4000
price = 5000

if price <= budget:
    print("This Item is within your budget")  #  A Tab spaces is necessary
else:
    print("This Item is not in your budget")


"""''Elif conditional statement"""
# elif is similar to else if in javascript

num1 = 0
if num1 > 0:
    print("Number is positive ")
elif num1 == 0:  # you can add many elif statement to check
    print("Number is Zero")
else:
    print("Number is negative")





""" Nested if  """
# We can use if, if-else, elif statements inside other if statements as well.



num = 13
if(num < 0 ):
    print('Number is negative')
elif(num > 0):
    if(num <=10):
        print('Number is between 1-10')
    elif(num > 10 and num <=20):
        print('Number is between 10-20')
    else:
        print('Number is greater than 20 ')
else:
    print('Number is zero')

