
### Explanation of the Solution

To implement the Eight Queens (8Q) task using **Method 3. Pipes-and-filters**. In Python, this pattern can be easily implemented with built-in methods and classes.

1. **position_generator** generates all possible positions for the queens, avoiding conflicts by using a recursive algorithm. Each valid arrangement of queens is sent to queue `q1`.
2. **conflict_checker** receives combinations from queue `q1`. Since `position_generator` already ensured no conflicts, it directly passes the solution to `q2`.
3. **solution_collector** reads solutions from queue `q2`, saves and prints each one. At the end, it prints the total count of solutions.

### How It Works

- **Queues** (`q1` and `q2`) are used as channels for passing data between filters, implementing the **Pipes-and-Filters** architecture.
- **Threads** (one for each filter) enable each step to run asynchronously without direct calls between filters.
- **End of Data** is indicated with `None`, letting each filter know when to complete its work.

In this way, we've implemented a **Pipes-and-Filters** architecture, where each filter is independent and interacts with others only through queues, aligning with the method's requirements.

Each solution is displayed as a list of 8 numbers, where each number indicates the position of a queen in the corresponding row.

Example of result:
```
Solution: [0, 4, 7, 5, 2, 6, 1, 3]
Solution: [0, 5, 7, 2, 6, 3, 1, 4]
Solution: [0, 6, 3, 5, 7, 1, 4, 2]
Solution: [0, 6, 4, 7, 1, 3, 5, 2]
Solution: [1, 3, 5, 7, 2, 0, 6, 4]
Solution: [1, 4, 6, 0, 2, 7, 5, 3]
Solution: [1, 4, 6, 3, 0, 7, 5, 2]
Solution: [1, 5, 0, 6, 3, 7, 2, 4]
Solution: [1, 5, 7, 2, 0, 3, 6, 4]
Solution: [1, 6, 2, 5, 7, 4, 0, 3]
Solution: [1, 6, 4, 7, 0, 3, 5, 2]
Solution: [1, 7, 5, 0, 2, 4, 6, 3]
Solution: [2, 0, 6, 4, 7, 1, 3, 5]
Solution: [2, 4, 1, 7, 0, 6, 3, 5]
Solution: [2, 4, 1, 7, 5, 3, 6, 0]
Solution: [2, 4, 6, 0, 3, 1, 7, 5]
Solution: [2, 4, 7, 3, 0, 6, 1, 5]
Solution: [2, 5, 1, 4, 7, 0, 6, 3]
Solution: [2, 5, 1, 6, 0, 3, 7, 4]
Solution: [2, 5, 1, 6, 4, 0, 7, 3]
Solution: [2, 5, 3, 0, 7, 4, 6, 1]
Solution: [2, 5, 3, 1, 7, 4, 6, 0]
Solution: [2, 5, 7, 0, 3, 6, 4, 1]
Solution: [2, 5, 7, 0, 4, 6, 1, 3]
Solution: [2, 5, 7, 1, 3, 0, 6, 4]
Solution: [2, 6, 1, 7, 4, 0, 3, 5]
Solution: [2, 6, 1, 7, 5, 3, 0, 4]
Solution: [2, 7, 3, 6, 0, 5, 1, 4]
Solution: [3, 0, 4, 7, 1, 6, 2, 5]
Solution: [3, 0, 4, 7, 5, 2, 6, 1]
Solution: [3, 1, 4, 7, 5, 0, 2, 6]
Solution: [3, 1, 6, 2, 5, 7, 0, 4]
Solution: [3, 1, 6, 2, 5, 7, 4, 0]
Solution: [3, 1, 6, 4, 0, 7, 5, 2]
Solution: [3, 1, 7, 4, 6, 0, 2, 5]
Solution: [3, 1, 7, 5, 0, 2, 4, 6]
Solution: [3, 5, 0, 4, 1, 7, 2, 6]
Solution: [3, 5, 7, 1, 6, 0, 2, 4]
Solution: [3, 5, 7, 2, 0, 6, 4, 1]
Solution: [3, 6, 0, 7, 4, 1, 5, 2]
Solution: [3, 6, 2, 7, 1, 4, 0, 5]
Solution: [3, 6, 4, 1, 5, 0, 2, 7]
Solution: [3, 6, 4, 2, 0, 5, 7, 1]
Solution: [3, 7, 0, 2, 5, 1, 6, 4]
Solution: [3, 7, 0, 4, 6, 1, 5, 2]
Solution: [3, 7, 4, 2, 0, 6, 1, 5]
Solution: [4, 0, 3, 5, 7, 1, 6, 2]
Solution: [4, 0, 7, 3, 1, 6, 2, 5]
Solution: [4, 0, 7, 5, 2, 6, 1, 3]
Solution: [4, 1, 3, 5, 7, 2, 0, 6]
Solution: [4, 1, 3, 6, 2, 7, 5, 0]
Solution: [4, 1, 5, 0, 6, 3, 7, 2]
Solution: [4, 1, 7, 0, 3, 6, 2, 5]
Solution: [4, 2, 0, 5, 7, 1, 3, 6]
Solution: [4, 2, 0, 6, 1, 7, 5, 3]
Solution: [4, 2, 7, 3, 6, 0, 5, 1]
Solution: [4, 6, 0, 2, 7, 5, 3, 1]
Solution: [4, 6, 0, 3, 1, 7, 5, 2]
Solution: [4, 6, 1, 3, 7, 0, 2, 5]
Solution: [4, 6, 1, 5, 2, 0, 3, 7]
Solution: [4, 6, 1, 5, 2, 0, 7, 3]
Solution: [4, 6, 3, 0, 2, 7, 5, 1]
Solution: [4, 7, 3, 0, 2, 5, 1, 6]
Solution: [4, 7, 3, 0, 6, 1, 5, 2]
Solution: [5, 0, 4, 1, 7, 2, 6, 3]
Solution: [5, 1, 6, 0, 2, 4, 7, 3]
Solution: [5, 1, 6, 0, 3, 7, 4, 2]
Solution: [5, 2, 0, 6, 4, 7, 1, 3]
Solution: [5, 2, 0, 7, 3, 1, 6, 4]
Solution: [5, 2, 0, 7, 4, 1, 3, 6]
Solution: [5, 2, 4, 6, 0, 3, 1, 7]
Solution: [5, 2, 4, 7, 0, 3, 1, 6]
Solution: [5, 2, 6, 1, 3, 7, 0, 4]
Solution: [5, 2, 6, 1, 7, 4, 0, 3]
Solution: [5, 2, 6, 3, 0, 7, 1, 4]
Solution: [5, 3, 0, 4, 7, 1, 6, 2]
Solution: [5, 3, 1, 7, 4, 6, 0, 2]
Solution: [5, 3, 6, 0, 2, 4, 1, 7]
Solution: [5, 3, 6, 0, 7, 1, 4, 2]
Solution: [5, 7, 1, 3, 0, 6, 4, 2]
Solution: [6, 0, 2, 7, 5, 3, 1, 4]
Solution: [6, 1, 3, 0, 7, 4, 2, 5]
Solution: [6, 1, 5, 2, 0, 3, 7, 4]
Solution: [6, 2, 0, 5, 7, 4, 1, 3]
Solution: [6, 2, 7, 1, 4, 0, 5, 3]
Solution: [6, 3, 1, 4, 7, 0, 2, 5]
Solution: [6, 3, 1, 7, 5, 0, 2, 4]
Solution: [6, 4, 2, 0, 5, 7, 1, 3]
Solution: [7, 1, 3, 0, 6, 4, 2, 5]
Solution: [7, 1, 4, 2, 0, 6, 3, 5]
Solution: [7, 2, 0, 5, 1, 4, 6, 3]
Solution: [7, 3, 0, 2, 5, 1, 6, 4]
Total Solutions: 92
```
