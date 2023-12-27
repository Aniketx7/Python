# Match case statement is similar to switch case in javascript 

x = 2

match x: 
    case 0:
        print('x is zero')
    case 2:
        print('x is 2 ')
    case _:         # 'case _' is a default (no case match, then this default case )
        print(x)    

    

# case with if conditions
y = int(input('Enter number'))
match y:
    case 0: 
        print('y is zero')
    case _ if y > 20 and y < 50:
        print(' y is between 20 and 50 ')
    case _ if y > 50:
        print('Y is greater than 50')
    case _: 
        print(y) 