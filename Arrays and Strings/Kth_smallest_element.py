'''Find the kth smallest element in an unsorted array'''
import heapq

class Kth_Smallest:
    def __init__(self,arr,k):
        self.arr=arr
        self.k=k

    def find_kth_smallest(self):
        arr=list(map(lambda x:-x,self.arr))
        k=self.k
        hp=[]
        for i in range(k):
             heapq.heappush(hp,arr[i])
        for j in range(i+1,len(arr)):
            if arr[j]<hp[0]:
                heapq.heappushpop(hp,arr[j])

        return hp[0]*-1

if __name__=='__main__':
    arr=[7, 10, 4, 3, 20, 15]
    k=4
    obj=Kth_Smallest(arr,k)
    print(obj.find_kth_smallest())