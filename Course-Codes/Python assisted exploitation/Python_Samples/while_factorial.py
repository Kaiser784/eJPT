# eLearnSecurity 2013

user_value = int(input("Insert a number: "))
res = 1
if user_value == 0:
    pass
else:
    while user_value != 0:

        #multiply res with user_value
        #and store the result into res
        res *= user_value

        #decrement user_value by 1
        user_value -= 1
print("Result is: ",res)
