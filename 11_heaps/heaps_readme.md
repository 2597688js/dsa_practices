# Heaps

## What is a Heap?

A **heap** is a specialized tree-based data structure that satisfies the heap property:
- **Min Heap**: Parent node is smaller than or equal to its children
- **Max Heap**: Parent node is greater than or equal to its children

Heaps are commonly implemented as **binary heaps** using a list/array where:
- Parent of node at index `i` is at `i // 2`
- Left child of node at index `i` is at `2*i + 1`
- Right child of node at index `i` is at `2*i + 2`

**Key operations**: insert (O(log n)), delete/extract min/max (O(log n)), peek min/max (O(1))

## Python Implementation

Python provides the `heapq` module for min heaps:

```python
import heapq

# Create a min heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)

# Extract minimum
min_val = heapq.heappop(heap)  # 1
print(min_val)

# Peek at minimum without removing
print(heap[0])  # 3

# Create heap from list
data = [9, 5, 6, 2, 3]
heapq.heapify(data)  # In-place: O(n)
print(data)  # [2, 3, 6, 5, 9]
```

For **max heap**, negate values:
```python
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
print(-heapq.heappop(max_heap))  # 5
```

## Common Use Cases

- Priority queues
- Heap sort
- Finding k smallest/largest elements
- Dijkstra's algorithm
- Huffman coding
