#
def divide(ourdividend,ourdivisor):
    sign=(-1 if((ourdividend<0)^(ourdivisor<0)) else 1)#Check if divisor is positive or negative
    #Make both positive
    ourdividend=abs(ourdividend) 
    ourdivisor=abs(ourdivisor)
    q=0
    temp=0
    #GO from 31 to 0 and accumulate all valid 
    for i in range(31,-1,-1):
        if(temp+(ourdivisor<<i)<=ourdividend):
            temp+=ourdivisor<<i
            q|=1<<i
    #Assuming the sign value computed earlier is -1, negate the quotient value
    if sign==-1:
        q=-q
    return q
a=int(input('Enter a for a/b'))
b=int(input('Enter b for a/b'))
print('Result of ',a,'/',b,'is',divide(a,b))
    