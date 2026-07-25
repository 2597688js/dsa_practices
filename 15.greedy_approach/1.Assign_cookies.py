"""
Author : janarddan
File_name = 1.Assign_cookies.py
Date : 19/07/26
Description :
Problem (LeetCode 455)

You have:

g[i] = greed factor of each child (minimum cookie size they need)
s[i] = size of each cookie

A child is satisfied if

cookie >= greed

Each cookie can be given to only one child.

Return the maximum number of satisfied children.

Example
g = [1,2,3]
s = [1,1]

Child greed:

1
2
3

Cookies:

1
1

We can satisfy only the first child.

Answer:

1

"""

g = [1, 3, 2]  # children greed factor
s = [1, 1]     # cookie size

g.sort()
s.sort()

print(g)
print(s)

child = 0 # pointer for children
cookie = 0 # pointer for cookies

# Continue while there are children and cookies left
while child < len(g) and cookie < len(s):

    # Can the current cookie satisfy the current child?
    if s[cookie] >= g[child]:
        # Yes, the child is satisfied
        child += 1

    # Move to the next cookie
    # (Whether it was used or too small)
    cookie += 1

# Number of satisfied children
print(child)