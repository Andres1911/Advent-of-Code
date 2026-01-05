import os
import numpy as np
from numpy.typing import NDArray
CWD = os.getcwd()
PATH = os.path.join(CWD, "source_7.txt")

def parse_source_file():
    with open(PATH, mode="r") as f:
        input = f.read()
        grid = input.split('\n')

    grid = [list(line) for line in grid]
    return np.array(grid)

def create_beam(grid: NDArray) -> tuple[NDArray, int]:
    split_count = 0
    source = np.where(grid[0] == 'S')
    for row in range(1, len(grid)):
        splitters = np.where(grid[row, :] == '^')
        common = np.intersect1d(splitters, source) # beam and splitter intersect
        beam_pass = np.setdiff1d(source, common)

        for beam in common:
            grid[row, beam - 1] = '|'
            grid[row, beam + 1] = '|'
            split_count += 1

        for beam in beam_pass:
            grid[row, beam] = '|'
        
        source = np.where(grid[row] == '|')
    
    with open(os.path.join(CWD, 'output_7.txt'), mode='w') as f:
        for row in grid:
            f.write(''.join(row) + '\n')

    return grid, split_count

from functools import lru_cache

def count_timelines(grid: NDArray) -> int:
    rows, cols = grid.shape
    grid_tuple = tuple(map(tuple, grid))  # Make hashable for cache
    
    @lru_cache(maxsize=None)
    def dfs(row: int, col: int) -> int:
        # Out of bounds or empty = end of path
        if row >= rows or col < 0 or col >= cols:
            return 1
        
        char = grid_tuple[row][col]
        
        if char == '.' or char == ' ':
            return 1  # End of path
        elif char == '^':
            # Split: sum paths from both branches
            return dfs(row + 1, col - 1) + dfs(row + 1, col + 1)
        elif char == '|':
            # Continue straight
            return dfs(row + 1, col)
        else:
            return 1  # Unknown char = end
    
    # Find start
    start_col = np.where(grid[0] == 'S')[0][0]
    result = dfs(1, start_col)
    
    print(f"Cache stats: {dfs.cache_info()}")
    return result


grid = parse_source_file()
grid, split_count = create_beam(grid)
paths = count_timelines(grid)
print(f"The number of splits is: {split_count}")
print(f"The number of paths is: {paths}")