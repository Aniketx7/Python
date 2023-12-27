# for loop in python
# for loops can iterate a sequence of iterable objects in python. iterating over a sequence is nothing but iterating over strings, list, tuples, sets and dictionaries

# Ex: Iterating over a string
a = "Aniket"
for i in a:
    print(i)

for i in a:
    print(i, end=", ")  # end is used to give the ending to object
    # output A, n, i, k, e, t


print('******************')



# Ex: Iterating over a List     and nesting in it 
colors = ["red", "Green", "Yellow", "blue"]
for color in colors:            
    print(color)            #return the string in list colors
    for i in color:
        print(i)            #print each character of string in color



print('******************')


#range - use 'for loop' for a specific number of times
''' for k in range(start, stop, step):      # step means interval 
    ...      
 '''


for k in range(5):
    print(k)        #print 0 to 4 

# end is used to give the ending to object
for k in range(4, 9):
    print(k)      #output: from 4 to 8

print('******************')

for k in range(2, 27, 5):
    print(k)            #output: from 2 to 27 with a interval of 5          like: 7, 12, 17, 22


