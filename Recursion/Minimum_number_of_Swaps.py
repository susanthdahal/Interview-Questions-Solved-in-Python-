'''Given an array and the corresponding pair of items in the array
find the minimum no of swaps required for arranging pairs adjacent to each other'''


def make_dict(arr):
    index={}
    for ind,val in enumerate(arr):
        index[val]=ind
    return index


def find_minimum_swaps(arr,pairs,index,current):
    if current==len(arr):
        return 0


    val1=arr[current]
    val2=arr[current+1]
    pairv1=pairs[val1]
    pairv2=pairs[val2]

    if pairv1==val2:
        return find_minimum_swaps(arr,pairs,index,current+2)
    else:
        ind1=index[val1]
        ind2=index[val2]
        ind3=index[pairv1]
        ind4=index[pairv2]

        index[val1],index[pairv2]=index[pairv2],index[val1]
        arr[ind1],arr[ind4]=arr[ind4],arr[ind1]

        swap1=find_minimum_swaps(arr,pairs,index,current+2)

        index[val1], index[pairv2] = index[pairv2], index[val1]
        arr[ind1], arr[ind4] = arr[ind4], arr[ind1]

        index[val2], index[pairv1] = index[pairv1], index[val2]
        arr[ind2], arr[ind3] = arr[ind3], arr[ind2]

        swap2=find_minimum_swaps(arr, pairs, index, current + 2)

        index[val2], index[pairv1] = index[pairv1], index[val2]
        arr[ind2], arr[ind3] = arr[ind3], arr[ind2]

        return 1+min(swap1,swap2)



if __name__ =='__main__':
    arr=[3,5,6,4,1,2]
    pairs={}
    pairs[1]=3
    pairs[3]=1
    pairs[2]=6
    pairs[6]=2
    pairs[4]=5
    pairs[5]=4
    index = make_dict(arr)
    current=0
    print(find_minimum_swaps(arr,pairs,index,current))



