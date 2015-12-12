# Advent of Code: Day 12
import re
import json

with open('day12.data') as f:
    string = f.read()


# Part 1
print "Day12 part 1:", sum(map(int, re.findall("-?[0-9]+", string)))


# Part 2
def hook(obj):
    if "red" in obj.values():
        return {}
    else: return obj

stuff = str(json.loads(string, object_hook=hook))
print "Day12 part 2:", sum(map(int, re.findall("-?[0-9]+", stuff)))
