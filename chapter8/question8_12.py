from functools import lru_cache


@lru_cache(maxsize=None)
def remove_location(place, n_grid):
    to_remove = set()

    # marked row and colums
    for i in range(0, n_grid):
        to_remove.add('{},{}'.format(i, place[0]))
        to_remove.add('{},{}'.format(place[2], i))

    r, c = int(place[0]), int(place[2])
    # remove upwards diag
    while r < n_grid and c < n_grid:
        to_remove.add('{},{}'.format(r, c))
        r, c = r + 1, c + 1

    r, c = int(place[0]), int(place[2])
    # remove downwards diag
    while r >= 0 and c >= 0:
        to_remove.add('{},{}'.format(r, c))
        r, c = r - 1, c - 1

    return to_remove


def place_queens(places_left, n_queens, n_grid, cur=None, paths=None):
    if cur is None:
        cur = []

    if paths is None:
        paths = []

    if len(cur) == n_queens:
        # come back later to make sure unique maybe sort before add?
        paths.append(cur)
        return paths

    if not places_left or len(places_left) < n_queens - len(cur):
        return paths

    for place in sorted(places_left):
        new_left = places_left - remove_location(place, n_grid)

        place_queens(new_left, n_queens, n_grid, cur + [place], paths)

    return paths


@lru_cache(maxsize=None)
def gen_paths(n):
    paths = set()
    for r in range(0, n):
        for c in range(0, n):
            paths.add('{},{}'.format(r, c))
    return paths


def main():
    paths = gen_paths(8)
    queen_locs = place_queens(paths, 5, 8)
    #print(queen_locs)


if __name__ == '__main__':
    main()
