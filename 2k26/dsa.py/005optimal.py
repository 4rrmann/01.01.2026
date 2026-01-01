from math import sqrt

def fcators(n):
    num = n
    result = []
    for i in range(1, int(sqrt(num))+1):
        if num%i == 0:
            result.append(i)
            
            if i != num // i: #eg: not valid for 6 = 36 // 6 {hence, no repeating digits}
                result.append(num//i)

    return sorted(result)

n = int(input("enter a number: "))
print(f"factors: {fcators(n)}")

# time Complexity: O( sqrt(n) )
# space Complexity: O(k) --> k would be the total no. of factors