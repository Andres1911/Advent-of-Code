import os
from functools import lru_cache

CWD = os.getcwd()
PATH = os.path.join(CWD, "source_2.txt")
CACHE: dict[int, list[int]] = {}

def parse_source_file():
    with open(PATH, mode="r") as f:
        file = f.read()
    
    content = file.split(',')
    return content


def find_inrange_invalid_hard(content: list[str]):
    sum = 0
    for values in content:
        first, second = values.split('-')
        first_num, second_num = int(first), int(second) + 1
        for i in range(first_num, second_num):
            sum += find_repeated_nums(i)
        
    print(f"The final sum is: {sum}")
    return sum

@lru_cache(maxsize=32)
def find_divisors(n: int) -> tuple[int, ...]:
    """Find proper divisors of n (excluding n itself)."""
    if n <= 1:
        return ()
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i and n // i != n:
                divisors.append(n // i)
        i += 1
    return tuple(sorted(divisors, reverse=True))

def find_repeated_nums(n: int) -> int:
    num_str = str(n)
    num_digits = len(num_str)
    if num_digits < 2:
        return 0
    
    for div in find_divisors(num_digits):
        # Fast path: check first char repetition for div=1
        if div == 1:
            if num_str == num_str[0] * num_digits:
                return n
            continue
        
        # Avoid string multiplication - compare chunks
        pattern = num_str[:div]
        is_repeat = True
        for i in range(div, num_digits, div):
            if num_str[i:i + div] != pattern:
                is_repeat = False
                break
        
        if is_repeat:
            return n
    
    return 0

contents = parse_source_file()
find_inrange_invalid_hard(contents)
print(find_divisors.cache_info())