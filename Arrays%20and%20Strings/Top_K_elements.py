'''Find the top k elements in an array'''

import heapq

def find_top_k(arr,k):
    #arr=list(map(lambda x:-x,arr))
    hp=[]
    for i in range(k):
        heapq.heappush(hp,arr[i])

    for j in range(i+1,len(arr)):
        if arr[j]>hp[0]:
            heapq.heapreplace(hp,arr[j])

    return hp


if __name__=='__main__':
    arr = [2, 3, 4, 5, 6, 7, 10, 9, 8, 7]
    k=4
    print(find_top_k(arr,k))