''' Parntheses matching problem'''

def match(string, left,right):
    stack=[]
    for char in string:
        if char in left:
            stack.append(char)
        elif char in right:
            if len(stack)==0:
                return False
            elif right.index(char)!=left.index(stack.pop()):
                return False
    return not stack



if __name__=='__main__':
    string="((()(()){([()])}))"
    left="([{"
    right=")]}"
    print(match(string,left,right))
