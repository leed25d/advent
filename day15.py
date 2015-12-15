#
from collections import OrderedDict, defaultdict
import re
from itertools import product
from operator import mul

ingredients = OrderedDict()
line_re = '(\w+): capacity ([+-]?\d+), durability ([+-]?\d+), flavor ([+-]?\d+), texture ([+-]?\d+), calories ([+-]?\d+)'
for line in open('day15.data'):
    parsed = re.match(line_re, line).groups()
    ingredients[parsed[0]] = OrderedDict([('capacity', eval(parsed[1])),
                                          ('durability', eval(parsed[2])),
                                          ('flavor', eval(parsed[3])),
                                          ('texture', eval(parsed[4])),
                                          ('calories', eval(parsed[5])),
                                          ('quantity', 0)])


def i_combo(start, stop, total, places):
    for s in product(xrange(start, stop), repeat=places):
        if sum(s) == total:
            yield s

properties = ['capacity', 'durability', 'flavor', 'texture', 'calories']
makings = list(ingredients)
p_dict = defaultdict(int)


def compute_score(check_calories=0):
    max_score = None
    for s in i_combo(0, 101, 100, len(ingredients)):
        ##  s is tsp quantity for frosting, candy, butterscotch, sugar
        ##  respectively
        for k, q in zip(ingredients, s):
            ingredients[k]['quantity'] = q

        p_dict.clear()
        for prop, making in product(properties, makings):
            value = ((ingredients[making][prop]) * (ingredients[making]['quantity']))
            if prop == 'calories':
                if not check_calories:
                    continue
            p_dict[prop] += value

        if p_dict.get('calories', 500) != 500:
            continue
        max_score = max(max_score, reduce(mul, [p_dict[k] if p_dict[k] > 0 else 0 for k in p_dict if k != 'calories'], 1))
    return(max_score)

##  Part 1.  max_score is 18965440
print "Part 1.  max_score is %d" % compute_score()
## Part 2.  max_score is 15862900
print "Part 2.  max_score is %d" % compute_score(1)
