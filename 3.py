def is_aval(x):
    if(x == 1):
        return False
    if(x == 2):
        return True
    
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def find_aval(x):
    if(is_aval(x)):
        print(x)
    if(x == 1):
        return
    find_aval(x-1)

find_aval(100)