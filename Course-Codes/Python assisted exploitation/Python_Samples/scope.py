# eLearnSecurity 2013

x = 10

def test_scope(z):
    f = x + z
    return f

print("before test_scope x is",x)
print("result:",test_scope(2))
print("after test_scope x is",x)
