import re

part1, part2 = (0, 0)
in_file = "day8.data"
with open(in_file) as f:
    for line in f:
        line = line.strip()
        part1 += len(line) - len(eval(line))
        part2 += len(re.escape(line)) + 2 - len(line)

print "part 1:", part1
print "part 2:", part2
##                         A N S W E R S
##  (advent)lee@stx:/opt/python/virt/advent/advent$ python day8.py
##  part 1: 1350
##  part 2: 2085
##
