#1 to n:

def func(n):
    if n==0:
        return

    func(n-1)
    #back-tracking
    print(n)

func(5)