#factorial
a=int(input("Enter a number: "))
def fact(a):
    if a < 2 :
        return 1
    else:
        return a * (fact(a-1))

print("Factorial of" ,a,'is:',fact(5))