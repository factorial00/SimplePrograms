def power(x, y): 
    if y == 0: 
        return 1
    if y % 2 == 0: 
        return power(x, y // 2) * power(x, y // 2) 
    return x * power(x, y // 2) * power(x, y // 2) 

def power(x, y):   
    if y == 0: 
        return 1
    if y % 2 == 0: 
        return power(x, y // 2) * power(x, y // 2) 
    return x * power(x, y // 2) * power(x, y // 2) 

def order(x): 
    n = 0
    while (x != 0): 
        n = n + 1
        x = x // 10
    return n 

def isArmstrong(x): 
    n = order(x) 
    t = x 
    s = 0
    while (t != 0): 
        r = t % 10
        s = s + power(r, n) 
        t = t // 10
  return (sum1 == x) 
  
x = int(input("enter a number : "))
print(isArmstrong(x))
