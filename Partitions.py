from itertools import combinations, chain

#Permutations
def sum_to_nP(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_nP(n - i, size - 1, i):
            yield [i] + tail

#Combinations
def sum_to_nC(n):
    'Generate the series of integer lists which sum to a integer, n.'
    from operator import sub
    b, mid, e = [0], list(range(1, n)), [n]
    splits = (d for i in range(n) for d in combinations(mid, i)) 
    return (list(map(sub, chain(s, e), chain(b, s))) for s in splits)

print(list(sum_to_nP(12, 2)))

#writing n as a list of positive integers that sum to n.