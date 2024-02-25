"""
Author : Janarddan Sarkar
file_name : check_anagram.py 
date : 24-02-2024
description : LISTEN, SILENT are anagrams.
             abc, bca, cab are anagrams.

             if len(str1) != len(str2), they can not be anagrams.

Logic is : count the number of occurrence for each character in the first string.
           Then, iterate over the second string, for each character present, decrement the count.\
           if count for each character is 0, it's an anagram.

"""


def isAnagram(str1, str2):

    if len(str1) != len(str2):
        return False

    count_char_d = {}

    for s in str1:
        if s not in count_char_d.keys():
            count_char_d[s] = 1
        else:
            count_char_d[s] += 1

    for s in str2:
       if s in count_char_d.keys():
           count_char_d[s] -= 1

    print(count_char_d)

    if any(count_char_d.values()):
        return False
    else:
        return True


if __name__ == "__main__":
    print(isAnagram('LISTEN', 'SILENT'))
