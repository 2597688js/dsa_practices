"""
Author : janarddan
File_name = 5. Longest Repeating Character Replacement.py
Date : 16/07/26
Description :
LeetCode 424

Problem

You are given a string s consisting of uppercase English letters and an integer k.

You can replace at most k characters in the string with any other uppercase English letter.

Return the length of the longest substring you can obtain that contains only the same letter after performing at most k replacements.

Example 1
Input:
s = "ABAB"
k = 2

Output:
4

Explanation:
Replace the two 'A's with 'B's (or vice versa).
Result: "BBBB"
Example 2
Input:
s = "AABABBA"
k = 1

Output:
4

Explanation:
Replace one 'A' with 'B':

AABABBA
  ↓
AABBBBA

The longest repeating substring is "BBBB".

"""


def longestRepeating(s,k):
    if len(s) <= 1:
        return len(s)

    left = 0
    maxi = 0
    count = {}
    for right in range(len(s)):
        if s[right] not in count:
            count[s[right]] = 1
        else:
            count[s[right]] += 1

        curr_window_size = right - left + 1
        # Invalid window
        if curr_window_size - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1

        curr_window_size_after_shrinking = right - left + 1
        maxi = max(maxi, curr_window_size_after_shrinking)

    return maxi

if __name__ == '__main__':
    print(longestRepeating('ABAB',2))
    print(longestRepeating('AABABBA',1))
    print(longestRepeating('AC',0))
