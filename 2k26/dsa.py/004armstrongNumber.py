n = int(input("enter a number: "))

num = n
result = 0

count = len(str(n))
# print(f"{count} digits")
# count = 0

# while num>0:
#     count +=1
#     num = num//10

# print(f"{count} digits")
while num>0:
    last_digit = num%10
    result = result + last_digit**count
    num = num//10

if (n == result):
    print(f"yessir an armstrongNumber")
else:
    print(f"{result}? nah")

    
# time Complexity: O(log base(10) n)
# space Complexity: O(1) --> constant space