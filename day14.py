import re
from collections import defaultdict, OrderedDict

elapsed_seconds = 2503
reindeer = defaultdict(OrderedDict)
for line in open('day14.data'):
    parsed = re.match('(\w+) can fly (\d+) km/s for (\d+).*for (\d+).*', line).groups()
    reindeer[parsed[0]] = OrderedDict([('rate', int(parsed[1])),
                                       ('flight_time', int(parsed[2])),
                                       ('rest_time', int(parsed[3])),
                                       ('distance', 0),
                                       ('points', 0)])


def calc_distance(beast, elapsed):
    flight_time, rest_time, rate = beast['flight_time'], beast['rest_time'], beast['rate']
    (q, r) = divmod(elapsed, (flight_time + rest_time))

    distance = flight_time * rate * q
    if r >= flight_time:
        distance += flight_time * rate
    else:
        distance += r * rate
    return distance

max_distance = 0
for name in reindeer.keys():
    max_distance = max(max_distance, calc_distance(reindeer[name], elapsed_seconds))

print "part 1.  max_distance = %d" % max_distance


for t in range(1, elapsed_seconds):
    max_distance = 0
    for name in reindeer.keys():
        reindeer[name]['distance'] = calc_distance(reindeer[name], t)
        max_distance = max(max_distance, reindeer[name]['distance'])

    for name in reindeer.keys():
        if reindeer[name]['distance'] == max_distance:
            reindeer[name]['points'] += 1

print "part 2.  max_distance = %d" % max([reindeer[stag]['points'] for stag in reindeer.keys()])
