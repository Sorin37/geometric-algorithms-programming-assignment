def brute_force(H, P, d):
    """
    :param H: n (x, y) tuple of coordinates of the houses
    :param P: m (x, y) tuple of coordinates of the particles
    :param d: the unsafe distance from the house
    :return: The particles that affect each house
    Complexity: O(n*m)
    """
    houses_dict = {}

    for h_x, h_y in H:
        houses_dict[(h_x, h_y)] = []
        for p_x, p_y in P:
            if infinity_norm_distance(h_x, h_y, p_x, p_y) <= d:
                houses_dict[(h_x, h_y)].append((p_x, p_y))

    return houses_dict

def infinity_norm_distance(x1, y1, x2, y2):
    return max([abs(x1-x2), abs(y1-y2)])