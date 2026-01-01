n = int(input("enter a number: "))

num = n
rev = 0

while num>0:
    last_digit = num%10
    rev = rev*10 +last_digit
    num = num//10

if (n == rev):
    print("Palandrome")
else:
    print("Not a Palandrome")

# time Complexity: O(log base(10) n)
# space Complexity: O(1) --> constant space