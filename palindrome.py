a=int(input('enter a number'))
r=0
c=a

while a>0:
    b=a%10
    r=(r*10)+b
    a=a//10
if r==c:
    print('it is a palindrome number')

else:
    print('it is not palindrome')

print('reverse of this number',r,'i want to fuck as bad as i want to breath')

