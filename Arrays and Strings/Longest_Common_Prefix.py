'''Longest Common prefix for group of strings'''
import sys

def find_lcp(my_list):
    min_length=int(sys.maxsize)
    for i in range(len(my_list)):
        if len(my_list[i])<min_length:
            min_length=len(my_list[i])
    root={}
    for j in range(len(my_list)):
        curr=root
        for k in range(len(my_list[j])):
            if k==min_length:
                break
            curr=curr.setdefault(my_list[j][k],{})
        curr["_end"]="_end"

    result=[]
    key=list(root.keys())

    while key[0]!="_end" and len(key)==1:
        result.append(key[0])
        root=root[key[0]]
        key=list(root.keys())

    return ''.join(result)



if __name__=='__main__':
    my_list=["geeksforgeeks", "geeks", "geek", "geeker"]
    print(find_lcp(my_list))
