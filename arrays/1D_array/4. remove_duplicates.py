"""
Author : Janarddan Sarkar
File_name = 4. remove_duplicates.py
Date : 28-02-2024
Description :
-------------------------------------------
Problem Statement:
Given an integer array sorted in non-decreasing order, remove the duplicates in place(meaning without using
additional data structures like sets or dictionaries, you can modify the original list by rearranging its
elements) such that each unique element appears only once. The relative order of the elements should
be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the
final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.

----------------------------------
Example 1:
Input: arr[1,1,2,2,2,3,3]
Output: arr[1,2,3,_,_,_,_]

Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after
assigning [1,2,3] in the beginning of the array.
---------------------------------
Example 2:
Input: arr[1,1,1,2,2,3,3,3,3,4,4]
Output: arr[1,2,3,4,_,_,_,_,_,_,_]

Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after
assigning [1,2,3,4] in the beginning of the array.
"""


# 1. Bruteforce approach
"""
Intuition: We have to think of a data structure that does not store duplicate elements. 
So can we use a Hash set? Yes! We can. As we know HashSet only stores unique elements.

Approach: 
1. Declare a HashSet.
2. Run a for loop from starting to the end.
3. Put every element of the array in the set.
4. Store size of the set in a variable K.
5. Now put all elements of the set in the array from the starting of the array.
6. Return K.


Time complexity: O(n*log(n))+O(n)  ; O(nlogn) for inserting into the set,
                                    O(n) for taking it out from the set and putting in the array again.
Space Complexity: O(n) 
"""


def removeDuplicatesBruteforce(arr):
    temp_set = list()  # I am doing it with a list, it can also be a set,
    # accordingly change the append method for set
    for e in arr:
        if e not in temp_set:
            temp_set.append(e)

    for i in range(len(temp_set)):
        arr[i] = temp_set[i]

    for j in range(len(temp_set), len(arr)):
        arr[j] = '_'

    print("Final array : ", arr)
    return len(temp_set)


# 1. Bruteforce - from take u forward
def removeDuplicates1(arr) -> int:
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])

    k = len(st)

    j = 0
    for x in st:
        arr[j] = x
        j += 1
    return k


# 3. Optimal solution
"""
Two pointers approach
Intuition: We can think of using two pointers ‘i’ and ‘j’, we move ‘j’ till we don’t get a number
 arr[j] which is different from arr[i]. As we got a unique number we will increase the i pointer and 
 update its value by arr[j]. 

Approach:
1.  Take a variable i as 0;
2. Use a for loop by using a variable ‘j’ from 1 to length of the array.
3. If arr[j] != arr[i], increase ‘i’ and update arr[i] == arr[j].
4. After completion of the loop return i+1, i.e size of the array of unique elements.

Complexity Analysis:
    Time Complexity: O(N), only one loop
    Space Complexity: O(1), No additional space
"""


def removeDuplicatesOptimal(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1

    print("Final array : ", arr)
    return i+1


if __name__ == "__main__":
    print(removeDuplicatesBruteforce([1, 1, 2, 2, 2, 3, 3]))
    print(removeDuplicatesBruteforce([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]))
    print()

    print(removeDuplicates1([1, 1, 2, 2, 2, 3, 3]))
    print(removeDuplicates1([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]))
    print()

    print(removeDuplicatesOptimal([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]))
