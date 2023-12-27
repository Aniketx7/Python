# while loop execute statements while the condition is True. As soon as the condition become False, the interpreter comes out of the while loop.
# Example 
n = 0
while(n<3):
    print(n)        #print from 0 to 2
    n += 1

print('') 
print('*************************')

# while loop in decrement order
count = 5
while(count > 0):
    print(count)        #outupt: 5, 4, 3, 2, 1   (decrement order)
    count -= 1


print('')
print('*************************')

# Else with while loop 
i = 0
while(i<4):
    print(i)
    i += 1
else:           #when your loop become false, this executed
    print("Your loop become false, That's why you are seeing this else")





# Emulation of do while loop 
while True:
    number = int(input('enter the number: '))
    print(number)
    if not number > 0:
        break