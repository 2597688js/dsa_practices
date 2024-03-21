"""
Author : Janarddan Sarkar
file_name : 14.find_missing_number.py 
date : 16-03-2024
description :
Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N.
Find the number(between 1 to N), that is not present in the given array.

Example 1:
    Input Format: N = 5, array[] = {1,2,4,5}
    Result: 3
    Explanation: In the given array, number 3 is missing. So, 3 is the answer.

Example 2:
    Input Format: N = 3, array[] = {1,3}
    Result: 2
    Explanation: In the given array, number 2 is missing. So, 2 is the answer.
"""

# 1. Bruteforce
"""
Naive Approach(Brute-force approach):
Intuition: For each number between 1 to N, we will try to find it in the given array using linear search. And if we don’t find any of them, 
we will return the number.

The algorithm steps are as follows:
    1. We will run a loop(say i) from 1 to N.
    2. For each integer, i, we will try to find it in the given array using linear search.
        2.1 For that, we will run another loop to iterate over the array and consider a flag variable to indicate if the element exists 
            in the array. Flag = 1 means the element is present and flag = 0 means the element is missing.
        2.2 Initially, the flag value will be set to 0. While iterating the array, if we find the element, we will set the flag to 1 and 
        break out from the loop.
    Now, for any number i, if we cannot find it, the flag will remain 0 even after iterating the whole array and we will return the number.
    
Time Complexity: O(N2), where N = size of the array+1.
Reason: In the worst case i.e. if the missing number is N itself, the outer loop will run for N times, and for every single number the inner loop will also run for approximately N times. So, the total time complexity will be O(N2).

Space Complexity: O(1)  as we are not using any extra space.
"""


def find_missing_number_bruteforce1(arr, n):
    for i in range(1, n+1):
        if i not in arr:
            return i


def find_missing_number_bruteforce2(arr, n):
    for i in range(1, n+1):
        flag = 0
        for x in arr:
            if i == x:
                flag = 1
                break

        if flag == 0:
            return i


# 2. Better approach (using Hashing)
"""
Better Approach (using Hashing):
Intuition:
    Using the hashing technique, we will store the frequency of each element of the given array. Now, the number( i.e. between 1 to N) for which 
    the frequency will be 0, will be returned. 
    
Approach:
The algorithm steps are as follows:
    1.The range of the number is 1 to N. So, we need a hash array of size N+1 (as we want to store the frequency of N as well).
    2.Now, for each element in the given array, we will store the frequency in the hash array.
    3.After that, for each number between 1 to N, we will check the frequencies. And for any number, if the frequency is 0, we will return it.
    
Time Complexity: O(N) + O(N) ~ O(2*N),  where N = size of the array+1.
Reason: For storing the frequencies in the hash array, the program takes O(N) time complexity and for checking the frequencies in the second step again O(N) is required. So, the total time complexity is O(N) + O(N).

Space Complexity: O(N), where N = size of the array+1. Here we are using an extra hash array of size N+1.
"""
def find_missing_number_better(arr, N):
    hash_dict = {}
    for i in range(1, N+1):       # O(N)
        hash_dict[i] = 0

    for x in arr:                # worst case - O(N)
        if x in hash_dict:
            hash_dict[x] = hash_dict[x] + 1

    missing_num = [k for k in hash_dict if hash_dict[k] == 0]       # O(N)   So total O(3N) ~ O(N)
    return missing_num


def missingNumber_better(a, N):
    hash = [0] * (N + 1)  # hash array

    # storing the frequencies:
    for i in range(N - 1):
        hash[a[i]] += 1

    # checking the frequencies for numbers 1 to N:
    for i in range(1, N + 1):
        if hash[i] == 0:
            return i

    # The following line will never execute.
    # It is just to avoid warnings.
    return -1

# 3. Optimal solution 1
"""
Algorithm / Intuition
Summation Approach:
Intuition:
We know that the summation of the first N numbers is (N*(N+1))/2. We can say this S1. Now, in the given array, every number between 1 to N except 
one number is present. So, if we add the numbers of the array (say S2), the difference between S1 and S2 will be the missing number.
 Because, while adding all the numbers of the array, we did not add that particular number that is missing.
 
Approach:
The steps are as follows:
    1. We will first calculate the summation of first N natural numbers(i.e. 1 to N) using the specified formula.
    2. Then we will add all the array elements using a loop.
    3. Finally, we will consider the difference between the summation of the first N natural numbers and the sum of the array elements.
    
Complexity Analysis
    Time Complexity: O(N), where N = size of array+1.
    Reason: Here, we need only 1 loop to get the sum of the array elements. The loop runs for approx. N times. So, the time complexity is O(N).
    
    Space Complexity: O(1) as we are not using any extra space.
"""
def find_missing_number_optimal1(arr, N):
    ideal_sum = (N * (N+1)) / 2

    actual_sum = 0
    for x in arr:
        actual_sum += x

    missing_num = ideal_sum - actual_sum
    return missing_num

# 3. Optomal approach 2
"""
Algorithm / Intuition
XOR Approach:
Note: Among the optimal approaches, the XOR approach is slightly better than the summation one because the term (N * (N+1))/2 used in the
 summation method cannot be stored in an integer if the value of N is big (like 105). In that case, we have to use some bigger data types.
  But we will face no issues like this while using the XOR approach.

Intuition:
Two important properties of XOR are the following:

✌️XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
✌️XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2

Now, let’s XOR all the numbers between 1 to N.
xor1 = 1^2^…….^N

Let’s XOR all the numbers in the given array.
xor2 = 1^2^……^N (contains all the numbers except the missing one).

Now, if we again perform XOR between xor1 and xor2, we will get:
xor1 ^ xor2 = (1^1)^(2^2)^……..^(missing Number)^…..^(N^N)

Here all the numbers except the missing number will form a pair and each pair will result in 0 according to the XOR property. The result will be = 0 ^ (missing number) = missing number (according to property 2).

So, if we perform the XOR of the numbers 1 to N with the XOR of the array elements, we will be left with the missing number.

Approach:
The steps are as follows:
    1. We will first run a loop(say i) from 0 to N-2(as the length of the array = N-1).
    2. Inside the loop, xor2 variable will calculate the XOR of array elements i.e. xor2 = xor2 ^ a[i]. And the xor1 variable will calculate the 
       XOR of 1 to N-1 i.e. xor1 = xor1 ^ (i+1).
    3. After the loop ends we will XOR xor1 and N to get the total XOR of 1 to N.
    Finally, the answer will be the XOR of xor1 and xor2.
    
Complexity Analysis
    Time Complexity: O(N), where N = size of array+1.
    Reason: Here, we need only 1 loop to calculate the XOR. The loop runs for approx. N times. So, the time complexity is O(N).
    
    Space Complexity: O(1) as we are not using any extra space.
"""
def find_missing_number_optimal2(arr, N):
    ideal_xor_res = 0     # XOR of 1 to N
    actual_xor_res = 0    # XOR of the array elements
    for i in range(len(arr)):
        actual_xor_res = actual_xor_res ^ arr[i]
        ideal_xor_res = ideal_xor_res ^ (i + 1)

    # Till now ee have 1 ^ 2 ^ 3 ^ . . . (N-1), so we need to XOR the N
    ideal_xor_res = ideal_xor_res ^ N

    missing_num = actual_xor_res ^ ideal_xor_res

    return missing_num


if __name__ == "__main__":
    print("Bruteforce : ", find_missing_number_bruteforce1([1, 2, 4, 5], 5))
    print("Bruteforce : ", find_missing_number_bruteforce2([1, 2, 4, 5], 5))
    print("Better : ", find_missing_number_better([1, 2, 4, 5], 5))
    print("Better : ", missingNumber_better([1, 2, 4, 5], 5))
    print("Optimal : ", find_missing_number_optimal1([1, 2, 4, 5], 5))
    print("Optimal : ", find_missing_number_optimal2([1, 2, 4, 5], 5))
