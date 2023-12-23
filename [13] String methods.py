# String Methods
a = 'Hello world!'
b = '    Hello      google       '
c = 'Hello!>>>>>>'

# 1> upper()        -- Turn character into uppercase
print(a.upper())

# 2> lower()        --Turn characer into lowercase
print(a.lower())

# 3> strip()        --removes any whitespaces before and after the string       !middle spaces
print(b.strip())

# 4> rstrip()       --removes any trailing  characters  (only symbols)
print(c.rstrip('>'))

# 5> replace()      --replace all occurence of string with other string     (do not change original string)
print(a.replace('world', 'Aniket'))

# 6> split()        --jo instance diya gaya rahta hai waha waha pe string ko split kar deta hai (return new set )
print(a.split('r'))     #output: [hello wo', 'ld!']

# 7> capitalize()   --turn the first character of string to uppercase (other are turned lowercase) 
d = 'helLO compAny'
print(d.capitalize())

# 8> center()       --align the string to the center as per the parameter given by the user 
str1 = 'Welcome python developer'
print(str1.center(40))
    #can be provided padding character 
print(str1.center(32, '+'))         # output: ++++welcome python devleoper++++


# 9> count()        --returns the no. of times the given value has occured with the given string
a1 = 'hello myself'
print('In', a1,  ' `e` comes' ,a1.count('e'), 'times')


# 10> endswith()        --check if the string ends with given value 
a2 = 'Hii to myself'
print('[42]', a2.endswith('self'))
print('[43]', a2.endswith('sels'))

# can be also checked in between the value 
print('[46]', a2.endswith('to my', 2, 9))

# 11> find()        --searches for the first occurences in the string. If value is absent from string, return -1
str3 = 'His name is aniket, He is an honest man '
print('[50]', str3.find('is'))      #output: 1  ( there is 'is' in 'His')

print('[52]', str3.find('hello'))       #output: -1


#12> index()        --Searches for the first occurences in the string 
                        #raises exceptions for being absent of given value in string 
str4 = 'Hii python developer'
print('[58]', str4.index('pytho'))
# print(str4.index('web'))

    # difference b/w index() and find () - index raises an error if value is absent 


# 13> isalnum()     -- returns true only if the entire string only consists A-Z, a-z, 0-9   ( any character found, return false )
str5 = 'aij3ijtafkjkj325asfjaf'
print('[66]', str5.isalnum())

str6 = 'asdflkja;adskf, '
print('[69]', str6.isalnum())


# 14> isalpha()         -- if only A-Z, a-z consists, return true. otherwise false 
alpha = 'debug'             
print('[74]', alpha.isalpha())

nalpha = 'debug code'       #*** if spaces, return false 
print('[77]', nalpha.isalpha())



# 15> islower()         -- return true if entire string is in lowercase
low = 'code manipulation'
print('[83]', low.islower())


# 16> isspace()        -- return true only;if string contains only spaces
ws = '   '          #true 
ws2 = '     hii     '    #false
print('89]', ws.isspace())
print('[90]', ws2.isspace())


# 17> istitle()     --returns true only if first letter of all word of string is capitalized
cp = 'Welcome To my Comapny'        
print(cp.istitle())         #false
cp1 = 'Welcome To My Company'
print('[97]', cp1.istitle())

