"""
Author : janarddan
File_name = 2.lemonade_change.py
Date : 20/07/26
Description :

LeetCode 860 - Lemonade Change

Problem:
---------
You are selling lemonade, and each lemonade costs $5.

Customers pay one at a time with either:
- $5
- $10
- $20

Initially, you have NO money.

For each customer, return the correct change if possible.
If at any point you cannot provide the required change, return False.
If all customers receive the correct change, return True.

Example:
--------
Input:
    bills = [5, 5, 5, 10, 20]

Process:
    Customer 1 pays $5 -> Keep it.
    Customer 2 pays $5 -> Keep it.
    Customer 3 pays $5 -> Keep it.
    Customer 4 pays $10 -> Give back one $5.
    Customer 5 pays $20 -> Give back one $10 and one $5.

Output:
    True


Greedy Idea:
------------
Keep track of only:
    - Number of $5 bills
    - Number of $10 bills

We do not need to store $20 bills because they are never used as change.

Rules:
------
1. If customer pays $5:
      - No change required.
      - Increase count of $5 bills.

2. If customer pays $10:
      - Need to return one $5.
      - If no $5 bill is available, return False.
      - Otherwise:
            five -= 1
            ten += 1

3. If customer pays $20:
      - Need to return $15.
      - There are two possible ways:

            Option 1: $10 + $5   (Preferred)
            Option 2: $5 + $5 + $5

      Always prefer Option 1 because it saves more $5 bills for future
      customers. A $5 bill is more valuable since both $10 and $20 customers
      may require it as change.

      If neither option is possible, return False.

Why Greedy Works:
-----------------
Always preserve as many $5 bills as possible.

For example:

    five = 4
    ten = 1

Need to give $15.

Using:
    $10 + $5
Leaves:
    five = 3
    ten = 0

Using:
    $5 + $5 + $5
Leaves:
    five = 1
    ten = 1

The first option is better because future customers paying with $10 always
need a $5 bill for change.

Algorithm:
----------
For each bill:
    if bill == 5:
        keep it

    elif bill == 10:
        give one $5 if available

    else (bill == 20):
        first try to give $10 + $5
        otherwise give three $5 bills
        otherwise return False

If all customers are processed successfully,
return True.

Time Complexity:
----------------
O(n)

Space Complexity:
-----------------
O(1)

"""

def lemonade_change(bills):
    bills_d = {"five":0, "ten":0, "twenty":0}
    for bill in bills:
        if bill == 5:
            bills_d["five"] += 1

        elif bill == 10:
            if bills_d["five"] >= 1:
                bills_d["ten"] += 1
                bills_d["five"] -= 1
            else:
                return False
        elif bill == 20:
            if bills_d["ten"] >= 1 and bills_d["five"] >= 1:
                bills_d["five"] -= 1
                bills_d["ten"] -= 1
            elif bills_d["five"] >= 3:
                bills_d["five"] -= 3
                # bills_d["twenty"] += 1
            else:
                return False

    return True

if __name__ == '__main__':
    # bills = [5, 5, 5, 10, 20]
    # print(lemonade_change(bills))
    # bills1 = [10]
    # print(lemonade_change(bills1))
    bills2 = [5,5,20]
    print(lemonade_change(bills2))
