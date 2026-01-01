def factors(n):
    num = n
    result = []
    for i in range(1, num//2):
        if num%i == 0:
            result.append(i)
    result.append(num)
    return result

n = int(input("enter a number: "))
print(f"factors: {factors(n)}")

# time Complexity: O(n/2) = O(n)
# space Complexity: O(k) --> k would be the total no. of factors