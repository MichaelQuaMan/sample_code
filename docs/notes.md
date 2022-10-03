# Notes

# Sources

https://www.datasciencecentral.com/implementing-kd-tree-for-fast-range-search-nearest-neighbor/

https://en.wikipedia.org/wiki/K-d_tree

https://www.geeksforgeeks.org/program-determine-quadrant-cartesian-plane/

# Interesting Info

https://stackoverflow.com/questions/7507696/algorithm-for-placing-a-grid-over-a-disordered-set-of-points

# Snippet

## Creating single value from lat long

```python
from main import get_points_objects

if __name__ == "__main__":
    d = {}
    pts = get_points_objects(n_pts=10)
    for p in pts:
        sum_coord = p.x + p.y
        print(f"{p}: p.x + p.y: {sum_coord}")
        if d.get(sum_coord):
            d[sum_coord] += 1
            raise ValueError("Should not be any duplicates")
        else:
            d[sum_coord] = 1
```

## Bin data example

```python
"""
https://python-course.eu/numerical-programming/binning-in-python-and-pandas.php
"""
from collections import Counter


def create_bins(lower_bound, width, quantity):
    """ create_bins returns an equal-width (distance) partitioning.
        It returns an ascending list of tuples, representing the intervals.
        A tuple bins[i], i.e. (bins[i][0], bins[i][1])  with i > 0
        and i < quantity, satisfies the following conditions:
            (1) bins[i][0] + width == bins[i][1]
            (2) bins[i-1][0] + width == bins[i][0] and
                bins[i-1][1] + width == bins[i][1]
    """

    bins = []
    start = lower_bound
    stop = lower_bound + quantity * width + 1
    step = width
    for low in range(start, stop, step):
        bins.append((low, low + width))
    return bins


def find_bin(value, bins):
    """ bins is a list of tuples, like [(0,20), (20, 40), (40, 60)],
        binning returns the smallest index i of bins so that
        bin[i][0] <= value < bin[i][1]
    """

    for i in range(0, len(bins)):
        if bins[i][0] <= value < bins[i][1]:
            return i
    return -1


if __name__ == "__main__":
    print("-- Basic Example --")
    bins_eg = create_bins(lower_bound=10, width=10, quantity=5)
    print(bins_eg)

print("-- Fuller Example --")
bins_eg = create_bins(lower_bound=50, width=4, quantity=10)
print(bins_eg)

weights_of_persons = [
    73.4, 69.3, 64.9, 75.6, 74.9, 80.3,
    78.6, 84.1, 88.9, 90.3, 83.4, 69.3,
    52.4, 58.3, 67.4, 74.0, 89.3, 63.4
]

binned_weights = []

for v in weights_of_persons:
    bin_index = find_bin(v, bins_eg)
    print(v, bin_index, bins_eg[bin_index])
    binned_weights.append(bin_index)

frequencies = Counter(binned_weights)
print(frequencies)
```

### Output

```text
-- Basic Example --

[(10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70)]

-- Fuller Example --

[(50, 54), (54, 58), (58, 62), (62, 66), (66, 70), (70, 74), (74, 78), (78, 82), (82, 86), (86, 90), (90, 94)]

73.4 5 (70, 74)

69.3 4 (66, 70)

64.9 3 (62, 66)

75.6 6 (74, 78)

74.9 6 (74, 78)

80.3 7 (78, 82)

78.6 7 (78, 82)

84.1 8 (82, 86)

88.9 9 (86, 90)

90.3 10 (90, 94)

83.4 8 (82, 86)

69.3 4 (66, 70)

52.4 0 (50, 54)

58.3 2 (58, 62)

67.4 4 (66, 70)

74.0 6 (74, 78)

89.3 9 (86, 90)

63.4 3 (62, 66)

Counter({4: 3, 6: 3, 3: 2, 7: 2, 8: 2, 9: 2, 5: 1, 10: 1, 0: 1, 2: 1})
```

# Notes on Journey

https://en.wikipedia.org/wiki/Nearest_neighbor_search
What is it?

Saw word “R-Tree”

https://en.wikipedia.org/wiki/R-tree

What is it?

Looked at references and saw paper

http://www-db.deis.unibo.it/courses/SI-LS/papers/Gut84.pdf

Searched R-tree in Python
Found

https://rtree.readthedocs.io/en/latest/tutorial.html

Didn’t understand
Looked at
R-tree Spatial Indexing with Python – Geoff Boeing

https://geoffboeing.com/2016/10/r-tree-spatial-index-python/

### Looked at:

https://stackabuse.com/bucket-sort-in-python/

https://stackoverflow.com/questions/57838566/divide-my-data-into-a-grid-and-select-one-point-inside-each-box

https://betterprogramming.pub/making-grids-in-python-7cf62c95f413

http://andrewd.ces.clemson.edu/courses/cpsc805/references/nearest_search.pdf

https://stackoverflow.com/questions/4326332/what-is-the-difference-between-a-kd-tree-and-a-r-tree

https://github.com/stefankoegl/kdtree

https://rahvee.gitlab.io/comparison-nearest-neighbor-search/

https://en.wikipedia.org/wiki/Curse_of_dimensionality

# Freeze Reqs

```bash
pip list --format=freeze > requirements.txt
```
