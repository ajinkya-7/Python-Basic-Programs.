a=int(input('enter a number'))
for i in range(1,a+1):
    if a>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
    
