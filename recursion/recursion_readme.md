## Basic Syntax of Recursion
#### Every recursive function has two parts:
    - Base Case → Stops the recursion.
    - Recursive Case → Calls itself on a smaller version of the problem.
#### General template:
    ```python
    def recursive_function(parameters):
        # Base case
        if stopping_condition:
            return answer
    
        # Work (optional)
    
        # Recursive call
        return recursive_function(smaller_problem)
    ```


1. In recursion, we should have a base case.
ex: 4! = 4 x 3!
       = 4 x 3 x 2!
       = 4 x 3 x 2 x 1!
       = 4 x 3 x 2 x 1
  Here, 1! = 1 is the base case

2. Base case loi goi thakute Problem tu smaller hoi hoi goi thakibo lage. As in the above example, ami 4! k vagi vagi
  last t 1! loi goi palu.

3. Backtracking :
Printing from start to end in the Normal approach
printing is started in the end and ended in the starting is back tracking. i.e., actual code execution tu last
r falor pora start hoi. 


In normal recursion things happens while going in forward pass, while
in backtracking, things happens in coming back, that's why the term backtracking.