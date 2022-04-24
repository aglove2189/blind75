def twoSum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return d[target - n], i
        d[n] = i


if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == (0, 1)
    assert twoSum([3, 2, 4], 6) == (1, 2)
    assert twoSum([3, 3], 6) == (0, 1)
