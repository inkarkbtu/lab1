def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]

def has_33(nums):
    return any(nums[i] == 3 and nums[i+1] == 3 for i in range(len(nums) - 1))

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    from math import pi
    return (4/3) * pi * radius**3

def unique_elements(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result