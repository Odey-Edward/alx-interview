#!/usr/bin/python3
"""island_perimeter Module"""


def island_perimeter(grid):
    """returns the perimeter of the island
    described in grid"""
    lent = len(grid) - 1
    count = 0

    for i in range(1, lent):
        for y in range(1, len(grid[i]) - 1):
            if grid[i][y] == 1:
                if grid[i - 1][y] == 0:
                    count += 1
                if grid[i][y + 1] == 0:
                    count += 1
                if grid[i][y - 1] == 0:
                    count += 1
                if grid[i + 1][y] == 0:
                    count += 1
    return count
