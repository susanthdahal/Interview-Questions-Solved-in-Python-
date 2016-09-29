''' Find the longest Increasing Subsequence '''

#Binary Search
def ceilIndex(arr,low,high,key):
    while(high-low>1):
        mid=low+(high-low)//2
        if arr[mid]>=key:
            high=mid
        else:
            low=mid
    return high


def longest_inc_sub(array):
    length=1
    table=[0] * len(array)
    table[0]=array[0]
    for i in range(1,len(array)):
        if array[i]<table[0]:
            table[0]=array[i]
        elif array[i] > table[length-1]:
            table[length]=array[i]
            length+=1
        else:
            table[ceilIndex(table,-1,length-1,array[i])]=array[i]
    return length

if __name__=='__main__':
    array=[7, 2, 5, 7, 11, 8, 10, 6]
    print(longest_inc_sub(array))