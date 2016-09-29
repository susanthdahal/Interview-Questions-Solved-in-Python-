"""Given an Array of n elements pick maximum number of elements
from given array following the rule:-
we cannot pick A[i] and A[j] if absolute value of (A[i]-A[j]) > absolute value of (i-j)"""

def find(array):
    count=0
    for i in range(1,len(array)):
        for j in range(i):
            if abs(array[i]-array[j])<=abs(i-j):
                count+=2
    return count


if __name__=='__main__':
    arr=[13,5,4]
    print(find(arr))



