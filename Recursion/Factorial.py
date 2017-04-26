"""given a number return the factorial of the number"""
import sys
def Factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * Factorial(number - 1)


print(int(Factorial(int(sys.argv[1]))))
