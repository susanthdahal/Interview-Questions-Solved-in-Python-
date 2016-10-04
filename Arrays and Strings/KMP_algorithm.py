'''KMP algorithm for string matching'''

def compute_lps(pattern):
    j=0
    lps=[0]*len(pattern)
    i=1
    while i<len(pattern):
        if pattern[i]==pattern[j]:
            lps[i]=j+1
            j+=1
            i += 1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                lps[i]=0
                j+=1
                i+=1
    return lps

def kmp(pattern,text,lps):
    j=0
    i=0
    while i<len(text):
        if pattern[j]==text[i]:
            j+=1
            i+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
        if j==len(pattern):
            return i-len(pattern)
    return -1

if __name__=='__main__':
    pattern="abcaby"
    text="abxabcabcaby"
    lps=compute_lps(pattern)
    print(kmp(pattern,text,lps))
