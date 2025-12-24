import os
CWD = os.getcwd()
PATH = os.path.join(CWD, "source_3.txt")

def parse_source_file() -> list[int]:
    with open(PATH, mode="r") as f:
        content = [line.strip() for line in f]
    
    return content

def find_sum_joltage(nums: list[str]) -> int:
    sum = 0
    for num in nums:
        sum += find_largest_joltage_hard(num)

    return sum

def find_largest_joltage(n: str) -> int:
    first, second = '0', '0'
    for i, num in enumerate(n):
        if int(num) > int(first) and i != len(n) - 1:
            first = num
            second = '0'

        elif int(num) > int(second):
            second = num

    return int(first + second)

def find_largest_joltage_hard(n: str, num_digits: int = 12) -> int:
    pointers = ['0'] * num_digits
    if len(n) <= len(pointers):
        return n

    for i, num in enumerate(n):
        for j, ptr in enumerate(pointers):
            if int(num) > int(ptr) and len(n) - i >= num_digits - j:
                pointers[j] = num
                pointers[j + 1:] = [0] * (num_digits - (j + 1))
                break

    max_joltage = "".join(map(str, pointers))
    print(max_joltage)
    return int(max_joltage)

content = parse_source_file()
sum = find_sum_joltage(content)
print(f"The final joltage sum is: {sum}")