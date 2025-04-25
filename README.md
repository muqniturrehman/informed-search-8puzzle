# 8-Puzzle Problem: Informed Search Methods

This repository contains implementations of two informed search algorithms for solving the classic **8-puzzle problem**:

- **Best First Search (BFS)** using Manhattan Distance heuristic
- **A* (A-Star) Algorithm** using Manhattan Distance (and optionally Out-of-Place Tiles)

## 🧩 Problem Overview

The 8-puzzle consists of a 3x3 grid with tiles numbered 1 through 8 and one blank space (`' '`). The goal is to move the tiles into the correct order using the fewest moves possible.

### Goal State:

---

## 📁 Files

- `lab-2_BFS.py` – Implements **Best First Search** with Manhattan Distance.
- `lab-2_A_str.py` – Implements **A* Search** with g(n) + h(n), where:
  - g(n) = cost from the start node
  - h(n) = Manhattan Distance (number of steps to goal)

---

## 🔍 Heuristics Used

1. **Manhattan Distance**: Sum of the distances (in terms of moves) of each tile from its goal position.
2. **Out of Place Tiles** *(discussed in class but not implemented here, can be easily added)*: Number of tiles not in their correct place.

---

## ✅ Features

- Priority Queue for managing search frontiers using `heapq`
- Node class with path tracking (parent nodes)
- Pretty printed path from start to goal
- Efficient state checking using hashable string representations
- Separation of logic into clear functions (move generation, validation, etc.)

---

## 🧠 Algorithm Comparison

| Feature              | Best First Search          | A* Search                     |
|----------------------|----------------------------|-------------------------------|
| Cost Considered      | Only h(n) (heuristic)      | f(n) = g(n) + h(n)            |
| Memory Usage         | Lower                      | Slightly higher               |
| Path Optimality      | Not always optimal         | Always optimal (with admissible heuristic) |
| Explored Nodes       | Generally fewer than BFS   | More efficient in complex paths |

---
## Working Example

**Start State:**

```
4 7 8
3 6 5
1 2  
```

**Goal State:**

```
1 2 3
4 5 6
7 8  
```

### Sample Output (A* Algorithm)

```
Goal Reached

Step 0:
4 7 8
3 6 5
1 2  

Step 1:
4 7 8
3 6 5
1   2

Step 2:
4 7 8
3   5
1 6 2

...

Step N:
1 2 3
4 5 6
7 8  
```

> Number of steps and path may vary depending on algorithm and heuristic.

## Heuristic Used

- **Manhattan Distance** – Sum of the absolute distances of tiles from their goal positions.



## 🛠 How to Run

Ensure Python 3 is installed. Run the desired file:

```bash
BFS.py     # Best First Search
A_str.py   # A* Search
```

## Author

**Muqnit Ur Rehman**  
**Department Of Data Science FCIT(PUCIT)**

