from math import log10

def countDigits(num):
    return int(log10(num)) + 1

num = int(input("enter a number: "))
print(f"{countDigits(num)} digits")

# time Complexity: O(log base(10) n)
# space Complexity: O(1) --> constant space