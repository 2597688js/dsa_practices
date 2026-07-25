## Hash Table (Hash Map / Dictionary)

A hash table is a data structure that implements an associative array — a structure that maps keys to values 
using a **hash function** to compute an index into an array of buckets or slots.

### Key Properties
- **Fast lookups**: O(1) average time complexity
- **Key-value storage**: Each key maps to exactly one value
- **In Python**: Implemented as `dict`

### Simple Example

```python
# Create a hash table
student_grades = {}

# Insert/Update (O(1))
student_grades["Alice"] = 95
student_grades["Bob"] = 87

# Lookup (O(1))
print(student_grades["Alice"])  # Output: 95

# Delete (O(1))
del student_grades["Bob"]

# Check if key exists
if "Alice" in student_grades:
    print("Alice found")
```

### Why Hash Tables?
Instead of searching through a list in O(n) time, hash tables give you instant access to any value by its key in O(1) 
average time.

### Under the Hood
1. Hash function converts key → index
2. Value stored at that index
3. Collisions handled via chaining or open addressing