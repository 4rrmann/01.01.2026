#n to 1

def func(i,n):
    if i>n:
        return
    
    func(i+1, n)
    print(i)

func(1,5)