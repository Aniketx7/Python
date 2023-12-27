# Break and Continue in loop

# Break: loop ko break kar deta hai      loop se bahar chala jaata hai
# continue: Iteration ko skip kar deta hai           (jaise kisi loop me ek iteration ko print nahi karega OR SOMETHING)

# Example: _

for i in range(20):
    print("5 *", i, "=", 5 * i)
    if i == 11:  # Jab i = 11 hoga tab ye loop se bahar ho jayega
        print("yaha i = 11 ho gaya, so aap loop se bahar ho gaye ")
        break

print('')
print('**********************')

for i in range(8):
    if i == 4:                      #when i = 4, the iteration 4 will skipped
        print("Your i = 4 iteration skipped")                       
        continue
    print(i)  # you have to place 'continue' before printing it
