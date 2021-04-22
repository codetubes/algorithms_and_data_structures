# 5! = 5*4*3*2*1 = 5*4!
# 4! = 4*3*2*1 = 4*3!
# 0! = 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))