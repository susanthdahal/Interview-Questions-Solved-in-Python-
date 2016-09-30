'''Print all the permutation of a string'''

def list_to_string(strlist):
    return  ''.join(strlist)

def find_permutations(strlist, left,right):
    if left==right:
        print(list_to_string(strlist))
    else:
        for i in range(left,right+1):
            strlist[left],strlist[i]=strlist[i],strlist[left]
            find_permutations(strlist,left+1,right)
            strlist[left], strlist[i] = strlist[i], strlist[left]
    pass



if __name__ =='__main__':
    string="ABC"
    strlist=list(string)
    find_permutations(strlist,0,len(strlist)-1)
