import os
import numpy as np
from numpy.typing import NDArray
CWD = os.getcwd()
PATH = os.path.join(CWD, "source_4.txt")

DIR = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1], [1, 0], [1, 1],
]

def parse_source_file():
    with open(PATH, mode="r") as f:
        content = [[c for c in line.strip()] for line in f]
    
    return np.array(content)

def find_accessible_rolls(roll_map: NDArray[np.int64], padded_roll_map: NDArray[np.int64]) -> int:
    sum_toilet_paper = 0
    length, height = roll_map.shape
    coordinates = []
    for row in range(1, height + 1):
        for col in range(1, length + 1):
            if padded_roll_map[row][col] != '@':
                continue
            
            sum_rolls = 0
            for x, y in DIR:
                if padded_roll_map[row + x][col + y] == '@':
                    sum_rolls += 1
            
            if sum_rolls < 4:
                sum_toilet_paper += 1
                coordinates.append((row - 1, col - 1))

    return sum_toilet_paper, coordinates

def remove_toilet_papers(roll_map: NDArray[np.int64]):
    padded_roll_map = np.pad(roll_map, 1, constant_values='.')
    total_sum = 0
    sum_toilet_paper = np.nan
    while sum_toilet_paper != 0:
        sum_toilet_paper, coordinates = find_accessible_rolls(roll_map, padded_roll_map)
        for x, y in coordinates:
            roll_map[x][y] = '.'
            padded_roll_map[x + 1][y + 1] = '.'
        
        print(f"Removed toilet papers: ({len(coordinates)}, {sum_toilet_paper})")
        total_sum += sum_toilet_paper
    
    return total_sum

content = parse_source_file()
sum = remove_toilet_papers(content)
print(f"The total sum of accessible toilet papers is: {sum}")