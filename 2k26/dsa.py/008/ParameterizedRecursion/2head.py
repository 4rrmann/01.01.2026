#1 to n

# def func(i,n):
#     print(i)
#     if i == n:
#         return
    
#     # i +=1
#     func(i+1,n)

# func(1,5)

def func(i, n):
    if i > n:
        return
    
    print(i)
    func(i+1, n)

func(1,5)