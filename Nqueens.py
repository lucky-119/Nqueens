import numpy as np

count=0
def place(i,j):
    a[i,j]='1'

def bound(x,y):
    if(x<0 or y<0 or x>n-1 or y>n-1):
        return False
    return True

def check(x,y):
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

def compare(x,y):
    global count
    for i in range(0,n):
        for j in range(0,n):
            if(check(i,j)==True and (i!=x or j!=y)):
                place(i,j)
                p.append(i)
                q.append(j)
                count=count+1
                
def backtrack(x,y):
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

    

        
        
            
        
            
    
    





                                            #Create n*n array
                                            #Place a queen in a corner
                                            
