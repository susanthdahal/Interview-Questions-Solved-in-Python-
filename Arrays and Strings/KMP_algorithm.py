'''KMP algorithm for string matching'''

def compute_lps(pattern):
    j=0
    lps=[0]*len(pattern)
    for i in range(1,len(pattern)):
        while pattern[i]!=pattern[j] and j>0:
            j=lps[j-1]
        if pattern[i]==pattern[j]:
            lps[i]=j+1
            j+=1
        else:
            lps[i]=0
    return lps

def kmp(pattern,text,lps):
    j=0
    for i in range(len(text)):
        while j>0 and text[i]!=pattern[j]:
            j=lps[j-1]
        if text[i]==pattern[j]:
            j+=1
        if j==len(pattern):
            return i-(len(pattern)-1)
    return -1

if __name__=='__main__':
    pattern="abcaby"
    text="abxabcabcaby"
    lps=compute_lps(pattern)
    print(kmp(pattern,text,lps))
