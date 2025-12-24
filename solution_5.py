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
    parsed = []
    for r in ranges:
        s, e = r.split('-')
        parsed.append((int(s), int(e)))
    parsed.sort()
    
    merged = [parsed[0]]
    for start, end in parsed[1:]:
        last_start, last_end = merged[-1]
        
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return sum(e - s + 1 for s, e in merged)

ranges, items = parse_source_file()
sum = check_good_items(ranges, items)
print(f"The sum of good items is: {sum}")