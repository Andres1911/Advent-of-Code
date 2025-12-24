import os
CWD = os.getcwd()
PATH = os.path.join(CWD, "source_5.txt")

def parse_source_file():
    with open(PATH, mode="r") as f:
        ranges = []
        items = []
        first_space = False
        for line in f:
            if line == '\n':
                first_space = True

            elif not first_space:
                ranges.append(line.strip())
            
            else:
                items.append(line.strip())

    return ranges, items

def check_good_items(ranges: list[str], items: list[str]) -> int:
    sorted_ranges = sort_ranges(ranges)
    no_merges = False
    while not no_merges:
        merged = False
        for i, r1 in enumerate(sorted_ranges[:-1]):
            for j, r2 in enumerate(sorted_ranges[i + 1:]):
                if can_merge(r1, r2):
                    new_range = merge_range(r1, r2)
                    sorted_ranges[i] = new_range
                    sorted_ranges.remove(r2)
                    merged = True
                    break
            
            if merged:
                break
        
        if not merged:
            no_merges = True
    
    good_items = 0
    for r in sorted_ranges:
        s, e = r.split('-')
        s, e = int(s), int(e)
        good_items += (e + 1) - s

    return good_items
        

def can_merge(range_1: str, range_2: str) -> bool:
    start_1, end_1 = range_1.split('-')
    start_1, end_1 = int(start_1), int(end_1)

    start_2, end_2 = range_2.split('-')
    start_2, end_2 = int(start_2), int(end_2)

    return start_2 <= end_1

def merge_range(range_1: str, range_2: str) -> str:
    start_1, end_1 = range_1.split('-')
    start_1, end_1 = int(start_1), int(end_1)

    start_2, end_2 = range_2.split('-')
    start_2, end_2 = int(start_2), int(end_2)

    return str(start_1) + '-' + str(max(end_1, end_2))

def sort_ranges(ranges: list[str]) -> list[str]:
    sorted_ranges = sorted(ranges, key=lambda r: int(r.split('-')[0]))
    return sorted_ranges

ranges, items = parse_source_file()
sum = check_good_items(ranges, items)
print(f"The sum of good items is: {sum}")