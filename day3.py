import re
import math

with open("inputs/day3") as f:
    lines = f.readlines()
    grid = [line.strip() for line in lines]

positions = [(1, 0), (1, 1), (0, 1), (-1, 1), 
            (-1, 0), (-1, -1), (0, -1), (1, -1)]

def partnumber(grid, x, y):
    for dx, dy in positions:
        px, py = x + dx, y + dy
        if not px < 0 and not py < 0 and not px >= len(grid) and not py >= len(grid[0]):
            if not grid[px][py].isdigit() and not grid[px][py] == ".":
                return True
    return False

res = 0
partn = {}
for x, row in enumerate(grid):
    digits = re.finditer("[0-9]+", row)
    for digit in digits:
        digit_start, digit_end = digit.start(), digit.end()
        if partnumber(grid, x, digit_start) or partnumber(grid, x, digit_end-1):
            partn[(x, digit_start)] = int(digit.group(0))
            partn[(x, digit_end-1)] = int(digit.group(0))

def gear_ratio(grid, x, y):
    nums = set()
    for dx, dy in positions:
        px, py = x + dx, y + dy
        if not px < 0 and not py < 0 and not px >= len(grid) and not py >= len(grid[0]):
            if (px, py) in list(partn.keys()):
                nums.add(partn[(px, py)])
    return math.prod(nums) if len(nums) == 2 else 0

res = 0
for x, row in enumerate(grid):
    gears = re.finditer("[*]", row)
    for gear in gears:
        gear_start, gear_end = gear.start(), gear.end()
        res += gear_ratio(grid, x, gear_end-1)
print(res)
