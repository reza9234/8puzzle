# 8-Puzzle Solver

This repository contains a Python implementation of an 8-puzzle solver using the Breadth-First Search (BFS) algorithm. The 8-puzzle is a classic sliding puzzle that consists of a 3x3 grid with tiles numbered 1 through 8 and one blank space. The objective is to rearrange the tiles to match a target configuration, typically with the blank space in the bottom-right corner.

## Features

- **Algorithm**: Uses BFS to explore the shortest path to the solution.
- **Visualization**: Displays the best path and the number of moves required to reach the solution.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/reza9234/8puzzle.git
cd 8puzzle
```

### Usage

To run the 8-Puzzle solver, execute the following command in your terminal:

```bash
python 8-Puzzle.py
```
The program will display the steps to solve the puzzle, starting from the given initial state to the solved state.
### Example

Given the initial state:
```bash
[[8, 7, 6],
 [5, 4, 3],
 [2, 1, 0]]
```
![Screenshot (215)](https://user-images.githubusercontent.com/44943502/236250127-dc9b5b91-dbb0-4d69-b11e-7f50673c47f6.png)

The solver finds the optimal solution path to the solved state which used 13 moves:
```bash
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 0]]
```
![Screenshot (216)](https://user-images.githubusercontent.com/44943502/236250844-7aceb83a-9f57-4f4b-bc5e-0cf7f5a89429.png)
