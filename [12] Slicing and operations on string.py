#length of a string       -   len 
a = 'hello world!'
print('length:', len(a))


# slicing a string  -  take a piece from string called slicing 

print('print letter at 4th index: ', a[4])     #print letter at 4th index         

print('print string till 7th index: ', a[:7])      


print('print from 2nd index to 7th index: ', a[2:7])       


#ye index 1 se start then, as index 0 mante hue  picche jayega aur -5th index jaha  aayaega waha tak ko nahi print karga 
print('print from index 1 to between index -5: ', a[1:-5])                


print('print from 3rd index to length of string:  ',a[3:len(a)] )

print('ye last se do index ke beech ka string dega:', a[1:-3])                #Isme pehle last se 4th index pe jayega phir last se 3rd index pe jayega aur index ke beech ka string de dega 
# Note: last index is not includes

