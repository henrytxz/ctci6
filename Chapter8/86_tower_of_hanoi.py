cache = {}


def solution(n):
    if n < 1: return RuntimeError('Tower of Hanoi with {0} disk doesn\'t make sense => exit'.format(n))
    if n == 1: return [(0,2),]
    if n in cache:
        steps = cache[n]
    else:
        steps = solution(n-1)
    newsteps = []
    location_disk1 = 0
    towers = set(range(3))
    for (fr, to) in steps:
        other = (towers - {fr, to}).pop()
        newsteps.append((location_disk1, other))
        location_disk1 = other
        newsteps.append((fr, to))
    newsteps.append((location_disk1, 2))
    return newsteps

print solution(3)