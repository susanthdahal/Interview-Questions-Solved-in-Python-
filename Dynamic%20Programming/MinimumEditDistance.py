def minimum_edit(str1,str2):
    col=len(str1)+1
    row=len(str2)+1
    mat=[[1 for i in range(col)] for j in range(row) ]
    for i in range(row):
        mat[i][0]=i

    for i in range(col):
        mat[0][i]=i

    for i in range(1,row):
        for j in range(1,col):
            if str2[i-1]==str1[j-1]:
                mat[i][j]=mat[i-1][j-1]
            else:
                mat[i][j]=min(mat[i-1][j-1],mat[i][j-1],mat[i-1][j])+1

    return mat[len(str2)][len(str1)]


str1="abcde"
str2="adcdf"
print(minimum_edit(str1,str2))