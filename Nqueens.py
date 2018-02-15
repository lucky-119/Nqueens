import numpy as np

count=0

def bound(x,y):                                             #To check if (x,y) lies within matrix a
    if(x<0 or y<0 or x>n-1 or y>n-1):
        return False
    return True

def check(x,y):                                             #To check whether a queen can be placed at (x,y)
    for i in range(0,n):
        if(a[x,i]==1 or a[i,y]==1):
            return False
        if(bound(x+i,y+i)==True):
            if(a[x+i,y+i]==1):
                return False
        if(bound(x+i,y-i)==True):
            if(a[x+i,y-i]==1):
                return False
        if(bound(x-i,y+i)==True):
            if(a[x-i,y+i]==1):
                return False
        if(bound(x-i,y-i)==True):
            if(a[x-i,y-i]==1):
                return False
    return True

def compare(x,y):                                           #To find the positions in a matrix where a queen can be placed
    global count
    for i in range(0,n):
        for j in range(0,n):
            if(check(i,j)==True and (i!=x or j!=y)):
                a[i,j]=1
                if(x==-1):
                    p.append(i)
                    q.append(j)
                else:
                    p.insert(0,i)
                    q.insert(0,j)
                count=count+1
                
def backtrack(x,y):                                         #To backtrack to find other combinations so that there are n queens placed 
    global count
    a[x,y]=0
    count=count-1
    compare(x,y)
        
p=[]
q=[]
n=input()
a=np.zeros((n,n))
compare(-1,-1)
while(count<n):
     backtrack(p.pop(),q.pop())
print a

                                            
