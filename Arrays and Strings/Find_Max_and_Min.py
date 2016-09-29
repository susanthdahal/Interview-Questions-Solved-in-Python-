''' Find the smallest and the largest number in a list.
The list is sorted in two sections,one in ascending order and other in descending order.'''


def find_max_min(arr):
    smallest=arr[0] if arr[0]<arr[-1] else arr[-1]
    low=0
    high=len(arr)
    while low < high:
        mid=(low+high)//2
        if mid==len(arr)-1:
            return (smallest,arr[mid])
        elif arr[mid] >= arr[mid+1] and arr[mid]>=arr[mid-1]:
            largest=arr[mid]
            return (smallest,largest)
        elif arr[mid]<arr[mid+1] and arr[mid]>arr[mid-1]:
            low=mid
        else:
            high=mid
    pass

if __name__=='__main__':
    arr=[2,3,4,5,6,7,10,9,8,7]
    arr1=[5,4,3,2,1]
    arr2=[1,2,3,4,5]
    arr3=[2,5,9,12,50,30,20,10,0,-1]
    print(find_max_min(arr))
    print(find_max_min(arr1))
    print(find_max_min(arr2))
    print(find_max_min(arr3))