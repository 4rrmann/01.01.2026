n = int(input("enter a number: "))

num = n
count = 0

while num>0:
    # last_digit = num%10

    # count = count +1
    count +=1
    num = num//10

print(f"{count} digits")

# time Complexity: O(log base(10) n)
# space Complexity: O(1) --> constant space