'''Given two strings, write a method to check if one is a permutation of the other'''

def check_permutation(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    count_dictionary = {}
    for char in first_string:
        if char in count_dictionary:
            count_dictionary[char] += 1
        else:
            count_dictionary[char] = 1
    for char in second_string:
        if char in count_dictionary and count_dictionary[char] != 0:
            count_dictionary[char] -= 1
        else:
            return False

    return True

if __name__ == '__main__':
    print(check_permutation("dog", "god"))
    print(check_permutation("abc", "bcl"))
    print(check_permutation("abc", "bcc"))