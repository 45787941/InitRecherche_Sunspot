import math
import shapely.geometry as sg

def _intersect_union(a, b):
    height = len(a)
    width = len(a[0])

    intersection_card = 0
    union_card = 0

    for i in range(0, height):
        for j in range(0, width):
            if (a[i][j] != 0 or b[i][j] != 0):
                intersection_card += 1
            if (a[i][j] != 0 and b[i][j] != 0):
                union_card += 1

    return (intersection_card, union_card)

def jaccard(a, b):
    intersection_card, union_card = _intersect_union(a, b)
    return float(intersection_card) / union_card

def dice(a, b):
    intersection_card, union_card = _intersect_union(a, b)
    return float(2 * intersection_card) / (len(a) + len(b))

# Metric from "A Metric for Polygon Comparison and Building Extraction Evaluation"
# Janja Avbelj, Rupert Mu ̈ller, and Richard Bamler Fellow, IEEE
# Code from http://github.com/GeoBigData/polis
def polis(a, b):
    poly_a = sg.Polygon(a)
    poly_b = sg.Polygon(b)
    bndry_a, bndry_b = poly_a.exterior, poly_b.exterior
    return _polis_side(bndry_a.coords, bndry_b) + _polis_side(bndry_b.coords, bndry_a)

def _polis_side(coords, bndry):
    sum = 0.0
    for pt in (sg.Point(c) for c in coords[:-1]): # Skip the last point (same as first)
        sum += bndry.distance(pt)
    return sum/float(2*len(coords))

def euclidian(a, b):
    if (len(a) == len(b)):
        sum = 0
        for i in range(0, len(a)):
            xA, yA = a[i]
            xB, yB = b[i]
            dist  = math.sqrt(((xB - xA) ** 2) + ((yB - yA) ** 2))
            sum += dist ** 2
        return math.sqrt(sum)
    else:
        return -1
