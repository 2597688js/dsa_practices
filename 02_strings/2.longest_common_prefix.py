"""
Author : janarddan
File_name = 2.longest_common_prefix.py
Date : 17/08/26
Description :

Longest Common Prefix

Write a function that finds the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower", "flow", "flight"]
Output: "fl"

Example 2:
Input: strs = ["dog", "racecar", "car"]
Output: ""

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

"""

def longest_common_prefix(arr:list[str]):
    n = len(arr[0])  # length of the first string
    prefix = ""

    for i in range(n):
        char = arr[0][i]

        for strng in arr[1:]:
            if i >= len(strng) or strng[i] != char:
                return prefix

        prefix += char

    return prefix


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
    print(longest_common_prefix(["flower", "flow"]))


