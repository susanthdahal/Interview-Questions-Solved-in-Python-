''' Given a String find all the palindromic paritions'''


from collections import defaultdict

def palindromic_partitions(string):
    matrix=[[False for i in range(len(string))] for j in range(len(string))]
    maxlen=1
    for i in range(len(string)):
        matrix[i][i]=True

    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            matrix[i][i+1]=True
            maxlen=2

    for k in range(3, len(string)+1 ):
        for i in range(len(string)-k+1):
            j=i+k-1
            if matrix[i+1][j-1] and string[i]==string[j]:
                matrix[i][j]=True
                if k>maxlen:
                    maxlen=k


    my_dict=defaultdict(lambda :[])
    for i in range(len(string)):
        for j in range(len(string)):
            if matrix[i][j]:
                my_dict[j-i+1].append((i,j+1))

    my_list=list(string)
    for i in my_list:
        print(i +" ",end="")
    print()

    start=0
    end=len(string)
    for i in range(2,len(string)+1):
        for val in my_dict[i]:
            final_str=string[start:val[0]]+" "+ string[val[0]:val[1]]+" "+string[val[1]:end]
            print(final_str)
    

palindromic_partitions("madam")
