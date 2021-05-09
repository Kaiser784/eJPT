# eLearnSecurity 2013

def change_global():
    """ Return the sum """
    global x
    x = 1

x = 4

print("x before calling the function:",x)
change_global()
print("x after calling the function:",x)
