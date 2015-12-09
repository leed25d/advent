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

p_str = ""
for star in shortest_path:
    p_str += '%s%s' % ('->' if len(p_str) else '', star)
print "shortest.  %s: %d" % (p_str, shortest_distance)

for star in longest_path:
    p_str += '%s%s' % ('->' if len(p_str) else '', star)
print "longest.  %s: %d" % (p_str, longest_distance)
##                         A N S W E R S
##  shortest.  Arbre->Tambi->Snowdin->Faerun->Straylight->Norrath->AlphaCentauri->Tristram: 141
##  longest.  Arbre->Tambi->Snowdin->Faerun->Straylight->Norrath->AlphaCentauri->Tristram->Faerun->Norrath->Tambi->Straylight->Snowdin->Tristram->Arbre->AlphaCentauri: 736