# eLearnSecurity 2013

def a(x):
    print("Sum of ",x,"+",x)
    return x + x
def b(x):
    print("Mul of ",x,"*",x)
    return x * x
    
function_switch = {
  1: a,
  2: b,
}

user = int(input("""Select an operation:
1) sum
2) mul
"""))

if user in function_switch:
    x = int(input("Insert a number: "))
    result = function_switch[user](x)
    print("the result is:",result)
else:
    print("Wrong input")
