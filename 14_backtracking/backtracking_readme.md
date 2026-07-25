# Backtracking

Backtracking is an algorithmic technique that solves problems by trying out different solutions and abandoning a solution as soon as it realizes the solution does not work.

## Key Concepts
- Explore all possible solutions
- Abandon a solution as soon as it's determined to be non-viable
- Use recursive approach with base cases and recursive calls
- Often requires state management and restoration

## Common Problems (from roadmap)
1. **N-Queens Problem** - Place N queens on NxN chessboard such that no two queens attack
2. **Rat in a Maze** - Find path from start to end in a maze
3. **Word Search** - Search for a word in a 2D grid
4. **Sudoku Solver** - Solve Sudoku puzzle using backtracking
5. **Generate Parentheses** - Generate all valid combinations of N pairs of parentheses
6. **Subsets** - Generate all subsets of a set (with and without duplicates)
7. **Combination Sum I & II** - Find all unique combinations that sum to target
8. **Permutations** - Generate all permutations (with and without duplicates)

## Time Complexity
- Most backtracking problems have exponential time complexity O(N! or 2^N)
- Space complexity depends on recursion depth and storage

## Template Pattern
```python
def backtrack(path, choices):
    # Base case: reached a solution
    if is_solution(path):
        solutions.append(path)
        return
    
    # Try different choices
    for choice in choices:
        if is_valid(choice, path):
            path.append(choice)
            backtrack(path, remaining_choices)
            path.pop()  # Restore state (backtrack)
```

## Study Order
1. Start with simple problems (Generate Parentheses)
2. Move to N-Queens (2D grid problems)
3. Sudoku Solver (constraint satisfaction)
4. Word Search, Rat in Maze (path finding)
5. Subsets, Permutations (combination generation)
