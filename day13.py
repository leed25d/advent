##
import collections
import itertools
import re

partners = collections.defaultdict(int)
for line in open('day13.data'):
    parsed = re.match('(.*) would (.*) (\d+) happiness.*to (.*)\.', line).groups()
    feeling = int(parsed[2]) * (1 if parsed[1] == 'gain' else -1)
    partners[(parsed[0], parsed[3])] = feeling


def max_hapiness(people):
    most = None
    for arrangement in itertools.permutations(people):
        arrangement += (arrangement[0],)
        hapiness = 0
        for i in xrange(len(arrangement) - 1):
            hapiness += partners[(arrangement[i], arrangement[i + 1])]
            hapiness += partners[(arrangement[i + 1], arrangement[i])]
            most = max(hapiness, most)
    return most


people = set([p for (p, _) in partners.keys()])
print "part 1.  Max hapiness = %d" % (max_hapiness(people))

people |= set(['Lee'])
print "part 2.  Max hapiness = %d" % (max_hapiness(people))
