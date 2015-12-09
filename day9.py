import re
from itertools import permutations, tee


def pairwise(iterable):
    "s -> (s0, s1), (s1, s2), ..."
    a, b = tee(iterable)
    next(b, None)
    return(zip(a, b))

in_file = "day9.data"
stars = set()
distances = dict()

with open(in_file) as f:
    for line in f:
        p = re.match(r'([^\s]*)\sto\s([^\s]*)\s=\s([0-9]*)', line)
        try:
            star1, star2, distance = p.groups()
            s = frozenset((star1, star2))
            distances[s] = int(distance)
            stars |= s
        except:
            pass

shortest_path = 0
shortest_distance = None
longest_path = 0
longest_distance = None

for path in permutations(stars):
    path_distance = 0
    for star1, star2 in pairwise(path):
        path_distance += distances.get(frozenset((star1, star2)), 0)
    if shortest_distance is None or path_distance < shortest_distance:
        shortest_distance = path_distance
        shortest_path = path
    if longest_distance is None or path_distance > longest_distance:
        longest_distance = path_distance
        longest_path = path

print "shortest.  %s: %d" % ("->".join(shortest_path), shortest_distance)
print "longest.  %s: %d" % ("->".join(longest_path), longest_distance)

##
##  shortest.  Arbre->Tambi->Snowdin->Faerun->Straylight->Norrath->AlphaCentauri->Tristram: 141
##  longest.  Faerun->Norrath->Tambi->Straylight->Snowdin->Tristram->Arbre->AlphaCentauri: 736
