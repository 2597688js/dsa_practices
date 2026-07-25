"""
Author : Janarddan Sarkar
file_name : 1. reverse_vowels.py 
date : 24-05-2024
description : Python program that reverses the vowels in a given string
"""
def reverse_vowels(s):
    # Function to check if a character is a vowel
    def is_vowel(ch):
        return ch.lower() in 'aeiou'

    # Convert the string to a list to make it mutable
    s = list(s)

    # Initialize two pointers, one at the beginning and one at the end of the list
    left, right = 0, len(s) - 1

    # Loop until the two pointers cross each other
    while left < right:
        # Move the left pointer until a vowel is found
        while left < right and not is_vowel(s[left]):
            left += 1
        # Move the right pointer until a vowel is found
        while left < right and not is_vowel(s[right]):
            right -= 1

        # Swap the vowels
        s[left], s[right] = s[right], s[left]

        # Move the pointers closer to the center
        left += 1
        right -= 1

    # Convert the list back to a string and return it
    return ''.join(s)


def reverse_vowels_easy(s):
    # Create a list of vowels found in the string
    vowels = [ch for ch in s if ch.lower() in 'aeiou']

    # Convert the string to a list to make it mutable
    s_list = list(s)

    # Replace each vowel in the string with the vowels from the list in reverse order
    for i in range(len(s_list)):
        if s_list[i].lower() in 'aeiou':
            s_list[i] = vowels.pop()

    # Convert the list back to a string and return it
    return ''.join(s_list)

# Example usage:
input_string = "hello world"
result = reverse_vowels(input_string)
result = reverse_vowels(input_string)
print("Original string:", input_string)
print("String with reversed vowels:", result)
