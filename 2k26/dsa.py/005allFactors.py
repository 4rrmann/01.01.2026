n = int(input("enter a number: "))

num = n
print("factors: ")
while num>0:
    if(n%num == 0):
        print(f"{num}")
    num -=1

# time Complexity: O(n)
# space Complexity: O(k) --> k would be the total no. of factors