##
from itertools import tee, groupby
import string
import re


def trips(s):
    a, b, c = tee(s, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return (e for e in zip(a, b, c))


def inc_string(string):
    ary = list(string)
    ary[-1] = chr(ord(ary[-1]) + 1)
    for i in range(-1, -len(ary), -1):
        if ord(ary[i]) == ord('z') + 1:
            ary[i] = 'a'
            ary[i - 1] = chr(ord(ary[i - 1]) + 1)
        else:
            break
    if ord(ary[0]) == ord('z') + 1:
        raise ValueError, string + " cannot be incremented."
    return ''.join(ary)

alphabet_trips = set(trips(string.ascii_lowercase))


def is_valid_passwd(s):
    ##  condition 2: does the string contain 'i', 'o', or 'l'?
    if re.search(r'[oil]', s):
        return False
    ##  condition 1: is there a triple?
    tri_s = set(trips(s))
    if tri_s.isdisjoint(alphabet_trips):
        return False
    ##  condition 3: does the string contain two different
    ##  non-overlapping pairs of characters?
    l2 = [list(g) for k, g in groupby(s) if len(list(g)) > 1]
    if len(l2) < 2:
        return False
    return(True)


def next_password(s):
    password = s
    while True:
        password = inc_string(password)
        if is_valid_passwd(password):
            break
    return(password)


##                          T E S T    D A T A
##print "next password from %s is %s" % ('abcdefgh', next_password('abcdefgh'))
##print "next password from %s is %s" % ('ghijklmn', next_password('ghijklmn'))
print "part1. next password from %s is %s" % ('hxbxwxba', next_password('hxbxwxba'))
print "part2. next password from %s is %s" % ('hxbxxyzz', next_password('hxbxxyzz'))
##                            A N S W E R S
##  part1. next password from hxbxwxba is hxbxxyzz
##  part2. next password from hxbxxyzz is hxcaabcc
