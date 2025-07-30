# -----------------------------------------------------------------------------
# Program to find the nth minimum and nth maximum element in an array
from array import *

def nmin(s,index):
    sort_arr=s.sort()
    return s[index-1]
    
def nmax(s,index):
    s.sort(reverse=True)
    return s[index-1]

s=list(map(int,input('Enter the array : ').split()))
index=int(input('Enter the nth minimum (n)?'))
result_min=nmin(s,index)
result_max=nmax(s,index)
print("Nth Maximum : ",result_max)
print("Nth Minimum : ",result_min)

# -----------------------------------------------------------------------------
#Enter the array : 
#3 9 2 8 1
#Enter the nth minimum (n)?
#2
#Nth Maximum :  8
#Nth Minimum :  2
# -----------------------------------------------------------------------------
