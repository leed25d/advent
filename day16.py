import re
from operator import gt, lt, eq

part1_ticker = [["children: 3", eq],
                ["cats: 7", eq],
                ["samoyeds: 2", eq],
                ["pomeranians: 3", eq],
                ["akitas: 0", eq],
                ["vizslas: 0", eq],
                ["goldfish: 5", eq],
                ["trees: 3", eq],
                ["cars: 2", eq],
                ["perfumes: 1", eq]]

part2_ticker = [["children: 3", eq],
                ["cats: 7", gt],
                ["samoyeds: 2", eq],
                ["pomeranians: 3", lt],
                ["akitas: 0", eq],
                ["vizslas: 0", eq],
                ["goldfish: 5", lt],
                ["trees: 3", gt],
                ["cars: 2", eq],
                ["perfumes: 1", eq]]

with open('day16.data') as f:
    aunts = f.read().splitlines()


##  returns True or False to keep the line for further examination
##  keep the line if
##    --the field (children, cats, etc) is not in the line
##    --the field is in the line and it's value matches the elemet's
##      value with the op predicate
def checkit(elem, op, line):
    field, value = re.split(r'\W+', elem)
    pat = r'%s:\s+(\d+)' % field
    m = re.findall(pat, line)
    if len(m) == 0:
        return True
    if op(int(m[0]), int(value)):
        return True
    return False

ary = aunts[:]
for elem, op in part1_ticker:
    ary = [line for line in ary if checkit(elem, op, line)]
print "part 1. %s" % str(ary)

ary = aunts[:]
for elem, op in part2_ticker:
    ary = [line for line in ary if checkit(elem, op, line)]
print "part 2. %s" % str(ary)
