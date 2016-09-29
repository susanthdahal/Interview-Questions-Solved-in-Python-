'''Find the Maximum element from each subarray of size k'''

from collections import deque

def find_max(arr,k):
    dq=deque()
    for i in range(k):
        if len(dq)==0:
            dq.append(i)
        else:
            while len(dq)!=0 and arr[i]>arr[dq[(len(dq)-1)]]:
                dq.pop()
            dq.append(i)
    result=[]
    result.append(arr[dq[0]])
    for j in range(i+1,len(arr)):
        if (j-dq[0])>=4:
            dq.popleft()
        else:
            while len(dq)!=0 and arr[j]>arr[dq[(len(dq)-1)]]:
                dq.pop()
            dq.append(j)
        result.append(arr[dq[0]])
    return result

if __name__=='__main__':
    arr=[9,6,11,8,10,5,4,13,93,14]
    k=4
    print(find_max(arr,k))

