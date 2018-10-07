#projet euler 16
def sumdigit(number):
    b=str(number)
    S=0
    for k in range(len(b)):
        S+=int(b[k])
    return(S)

assert sumdigit(2**15)==26
assert sumdigit(2**1000)==1366
print('sumdigit(2**1000) = '+str(sumdigit(2**1000)))

#projet euler 22
L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def namescore():
    f=open('p022_names.txt','r')
    P=[]
    for line in f:
        P.append(line)
    listemot=str.split(P[0],'","')
    listemot[0]=listemot[0][1:len(listemot[0])]
    listemot[-1]=listemot[-1][0:len(listemot[-1])-1]
    listemot=sorted(listemot)
    S=0
    for k in range(len(listemot)):
        A=listemot[k]
        S+=score(A)*(k+1)
    return(S)

def score(word):   
        s=0
        for i in range(len(word)):
            a=0
            while word[i]!=L[a]:
                a+=1
            s+=a+1 
        return(s)


assert namescore()==871198282
print('namescore = ' + str(namescore()))

#projet euler 55

def ispalindromic(n):
    a=str(n)
    m=len(a)
    for i in range(m):
        if a[i]!=a[-1-i]:
            return(False)
    return(True)
    
def reverse(n):
    a=str(n)
    m=len(a)
    b=''
    for i in range(m):
        b+=a[-1-i]
    return(int(b))
    
def isLychrel(n):
    lim=0
    a=n
    while lim<50:
        if ispalindromic(a+reverse(a)):
            return(False)
        else: 
            a=a+reverse(a)
            lim+=1
    return(True)
    
def Lychrelnumberbelow(n):
    S=0
    for i in range(n):
        if isLychrel(i):
            S+=1
    return(S)
    
assert Lychrelnumberbelow(10000)==249
print('There are '+str(Lychrelnumberbelow(10000))+' Lychrel numbers below 10000')

























