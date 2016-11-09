'''Subset Sum Problem'''

def find_subset(my_list,n):
    mat=[[False for i in range(n+1)] for j in range(len(my_list))]

    for i in range(len(my_list)):
        mat[i][0]=True

    mat[0][my_list[0]]=True

    for i in range(1,len(my_list)):
        for j in range(n+1):
            if my_list[i]>j:
                mat[i][j]=mat[i-1][j]
            else:
                mat[i][j]=mat[i-1][j-my_list[i]]

    return mat[len(my_list)-1][n]



print(find_subset([1,4,2,3],9))

