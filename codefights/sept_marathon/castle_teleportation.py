def on_tower(x, y, tower_center, r1, r2):
    tx, ty = tower_center
    if ((x - tx) ** 2 + (y - ty) ** 2) < r1 ** 2:
        return 'On the tower'
    elif (x - tx) ** 2 + (y - ty) ** 2 < r2 ** 2:
        return 'On the walls'
    else:
        return ''

def castleInvasion(castle, destination):
    wlen, width, r1, r2 = castle
    wlen = float(wlen)
    width = float(width)
    x, y = destination
    inside_radius = wlen / 2 - width / 2
    outside_radius = wlen / 2 + width / 2
    sq_radius = wlen / 2
    tower_centers = [(-sq_radius, -sq_radius), (-sq_radius, sq_radius),
                     (sq_radius, -sq_radius), (sq_radius, sq_radius)]
    for tcenter in tower_centers:
        result = on_tower(x, y, tcenter, r1, r2)
        if result:
            return result

    if -inside_radius < x < inside_radius and \
                            -inside_radius < y < inside_radius:
        return "Inside the castle"
    elif inside_radius ** 2 <= x ** 2 + y ** 2 <= outside_radius ** 2 + (
        sq_radius - r2) ** 2:
        return "On the walls"
    else:
        return "Outside the castle"

# print castleInvasion([71, 2, 9, 25], [29, -29])

assert castleInvasion(castle=[10, 2, 3, 4], destination=[-5, 5]) == "On the tower"
assert castleInvasion(castle=[10, 2, 3, 4], destination=[6, 0]) == "On the walls"
assert castleInvasion(castle=[10, 2, 3, 4], destination=[0, 7]) == "Outside the castle"
assert castleInvasion(castle=[10, 2, 3, 4], destination=[3, 0]) == "Inside the castle"