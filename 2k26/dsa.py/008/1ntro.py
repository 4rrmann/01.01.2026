#basic function of recursion:
def func(count):
    if count == 4:
        return
    print('not me') #head recursion
    func(count + 1)

func(0)

print('\n')

def func(count):
    if count == 4:
        return
    func(count + 1) 
    print('zairen') #tail recursion
    
func(0)