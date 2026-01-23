def fact(n):

    if n==0 or n==1: #base-case
        return 1
    
    return n * fact(n-1) #flow

print(fact(4))

#Time Complexity: O(N)
#Space Complexity: O(N) --> Stack space