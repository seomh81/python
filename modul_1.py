def gugudan(n):
    x = 1
    if(type(n) != type(1)):
        return print('input type not integer')
    else :
        while (x < 10):
            print(n*x)
            x = x + 1
            if(x == 10):
                break
