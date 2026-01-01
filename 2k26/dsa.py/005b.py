# n = int(input("enter a number: "))

# num = n
# result = []

# for i in range(1, num+1):
#     if num%i == 0:
#         result.append(i)

# print(f"factors: {result}")

def factors(n):
    num = n
    result = []
    for i in range(1, num+1):
        if num%i == 0:
            result.append(i)
    return result

n = int(input("enter a number: "))
print(f"factors: {factors(n)}")

# time Complexity: O(n)
# space Complexity: O(k) --> k would be the total no. of factors