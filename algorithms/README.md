# Algorithms Utility Library  

The `algorithms` directory is a curated set of classical algorithms that are vital in various computational problems. These algorithms serve as building blocks for constructing more complex algorithms or solutions.

## Table of Contents

1. [Sorting (`sorting.py`)](#sorting)
2. [Searching (`searching.py`)](#searching)
3. [Dynamic Programming (`dynamic_programming.py`)](#dynamic-programming)
4. [Backtracking (`backtracking.py`)](#backtracking)

---

### Searching (`searching.py`)

Searching is the algorithmic process of finding specific items in a collection. It can be carried out on any data structure.

**Functions**:

- **`linear_search(arr, x)`**: 
  - Implements the Linear Search algorithm, which checks each element of the list sequentially until a match is found or the whole list has been searched.
  
- **`binary_search(arr, x)`**:
  - Implements the Binary Search algorithm, which searches a sorted array by dividing the search interval in half repetitively.

---

### Dynamic Programming (`dynamic_programming.py`)

Dynamic Programming offers an optimized approach to solving problems by breaking them down into simpler overlapping sub-problems.

**Functions**:

- **`knapsack(values, weights, capacity)`**: 
  - Implements the 0/1 Knapsack problem using dynamic programming. The objective is to fill the knapsack with items to achieve maximum total value without exceeding its capacity.

---

### Backtracking (`backtracking.py`)

Backtracking solves problems incrementally, building candidates towards solutions, and discarding a candidate as soon as it is determined not to lead to a feasible solution.

**Functions**:

- **`solve_sudoku(board)`**:
  - A classic puzzle-solving algorithm, this function attempts to fill a Sudoku board while adhering to the game's rules.

---

For each algorithm, ensure you refer to the respective file for more detailed documentation, usage examples, and further insights. Whether you're aiming to optimize a solution, search through large datasets, or solve intricate problems, this library provides robust tools for various computational challenges.