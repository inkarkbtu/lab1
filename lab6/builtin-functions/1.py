import time
import math

def multiply_list(a):
    return math.prod(a)

def count_case(txt):
    cntup = sum(1 for i in txt if i.isupper())
    cntlow = sum(1 for i in txt if i.islower())
    return f"Uppercase: {cntup}\nLowercase: {cntlow}"

def is_palindrome(txt):
    return "palindrome" if txt == txt[::-1] else "not palindrome"

def delayed_sqrt(num, milsec):
    time.sleep(milsec / 1000)
    return f"Square root of {num} after {milsec} milliseconds is {num ** 0.5}"

def all_true(mytup):
    return all(mytup)

print(multiply_list([1, 2, 3, 4, 5]))  
print(count_case("Hello World"))  
print(is_palindrome("radar"))  
print(delayed_sqrt(25100, 2123))  
print(all_true((True, True, False)))  
print(all_true((True, True, True))) 