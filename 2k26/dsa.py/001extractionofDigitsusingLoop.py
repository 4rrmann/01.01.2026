# n = 5873

# num = n
# while num>0:
#     last_digit = num%10
#     print(last_digit)
#     num = num//10

n = int(input("Enter a number: "))

num = n
rev = 0

while num>0:
    last_digit = num%10
    rev = rev*10 + last_digit
    num = num//10

print("Reversed number: ",rev)

# time Complexity: O(log base(10) n)
# space Complexity: O(1) --> constant space