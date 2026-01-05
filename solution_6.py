import os
import  numpy as np
from numpy.typing import NDArray
CWD = os.getcwd()
PATH = os.path.join(CWD, "source_6.txt")

def parse_source_file():
    with open(PATH, mode="r") as f:
        lines = f.readlines()
    
    operators = lines[-1]
    nums = []
    op_nums = []
    for i in range(len(operators)):

        if operators[i] != " " and op_nums:
            nums.append(op_nums)
            op_nums = []

        num_str = ""
        for j in range(len(lines) - 1):
            digit = lines[j][i]
            digit = "" if digit == " " else digit
            num_str += digit

        if num_str.isdigit():
            op_nums.append(int(num_str))

    nums.append(op_nums)
    operators = operators.strip().split()
    return nums, operators

def calculate_total(nums: list[list[int]], operators: list[str]) -> int:
    ops = {'*': np.prod, '+': np.sum}
    return sum(ops[op](nums[i]) for i, op in enumerate(operators))


inputs, operators = parse_source_file()
print(inputs)
tot_sum = calculate_total(inputs, operators)
print(f"The total sum is: {tot_sum}")
