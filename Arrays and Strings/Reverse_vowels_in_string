'''Reverse the vowels in a string'''

def reverse(string):
    vow=['a','e','i','o','u']
    if string=="":
        return ""
    
    mylist=list(string)
    vowels=[]
    for i in range(len(mylist)):
        if mylist[i] in vow:
            vowels.append(i)

    for i in range(len(vowels)//2):
        mylist[vowels[i]],mylist[vowels[len(vowels)-1-i]]=mylist[vowels[len(vowels)-1-i]],mylist[vowels[i]]

    return ''.join(mylist)



if __name__=='__main__':
    string="abesdeeeooouuu"
    print(reverse(string))
