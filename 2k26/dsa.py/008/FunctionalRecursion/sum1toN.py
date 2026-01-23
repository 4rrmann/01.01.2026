#Functional Recursion:
# -Create a flow
# -Create the base condition


def sum(n):

    if n==1: #base condition
        return 1
    
    return n +sum(n-1) #flow

# print(func(4))
x = sum(4)
print(x)

#Time Complexity: O(N)
#Space Complexity: O(N) --> Stack space