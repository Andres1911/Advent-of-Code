import os
import numpy as np
from numpy.typing import NDArray
CWD = os.getcwd()
PATH = os.path.join(CWD, "source_4.txt")

def parse_source_file():
    with open(PATH, mode="r") as f:
        content = [[c for c in line.strip()] for line in f]
    
    return np.array(content)

def find_accessible_rolls(roll_map: NDArray[np.int64], padded_roll_map: NDArray[np.int64]) -> int:
    is_roll = (roll_map == '@').astype(int)
    padded = np.pad(is_roll, 1, constant_values=0)
    
    # Sum all 8 neighbors using slicing
    neighbor_counts = (
        padded[:-2, :-2] + padded[:-2, 1:-1] + padded[:-2, 2:] +  # top row
        padded[1:-1, :-2] +                    padded[1:-1, 2:] +  # middle (no center)
        padded[2:, :-2]  + padded[2:, 1:-1]  + padded[2:, 2:]     # bottom row
    )
    
    accessible = is_roll & (neighbor_counts < 4)
    coordinates = list(zip(*np.where(accessible)))
    
    return accessible.sum(), coordinates

def remove_toilet_papers(roll_map: NDArray[np.int64]):
    padded_roll_map = np.pad(roll_map, 1, constant_values='.')
    total_sum = 0
    sum_toilet_paper = np.nan
    while sum_toilet_paper != 0:
        sum_toilet_paper, coordinates = find_accessible_rolls(roll_map, padded_roll_map)
        coords = np.array(coordinates)
        if len(coords) > 0:
            rows, cols = coords[:, 0], coords[:, 1]
            
            roll_map[rows, cols] = '.'
            padded_roll_map[rows + 1, cols + 1] = '.'
        
        print(f"Removed toilet papers: ({len(coordinates)}, {sum_toilet_paper})")
        total_sum += sum_toilet_paper
    
    return total_sum

content = parse_source_file()
sum = remove_toilet_papers(content)
print(f"The total sum of accessible toilet papers is: {sum}")