import os
CWD = os.getcwd()
PATH = os.path.join(CWD, "source.txt")

def parse_source_file():
    with open(PATH, mode="r") as f:
        file = f.readlines()
    
    return file

def count_position_resets(file: list[str], total_num: int = 0):
    count = 0
    for line in file:
        direction = line[0]
        number = int(''.join(c for c in line[1:] if c.isdigit()))
        
        total_num = (total_num + number if direction == 'R' else total_num - number) % 100
        if total_num == 0:
            count += 1
    
    return count

def count_all_zeros_passed(file: list[str], total_num: int = 50):
    count = 0
    for line in file:
        direction = line[0]
        number = int(''.join(c for c in line[1:] if c.isdigit()))

        count += number // 100
        number = number % 100

        prev_num = total_num
        total_num = (total_num + number if direction == 'R' else total_num - number) % 100
        
        if total_num == 0 or (prev_num != 0 and (
            (direction == 'R' and total_num < prev_num) or
            (direction == 'L' and total_num > prev_num)
        )):
            count += 1
            
    return count

file = parse_source_file()
print(count_position_resets(file, 50))
print(count_all_zeros_passed(file))