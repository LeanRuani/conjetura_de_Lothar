def lothar(n,c):
    while n > 1:
        c+=1
        if(n % 2==0):
            n = int(n/2)
        else:
            n = int(n*3+1)
    return (c)
           
n = int(input())
c=0
print( lothar(n,c) )
