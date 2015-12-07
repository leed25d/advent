##
import itertools
import hashlib
import re

key = 'bgvyzdsv'
##key = 'pqrstuv'
##key = 'abcdef'

for i in itertools.count():
    h = hashlib.new('md5')
    h.update(key + str(i))
    if re.match(r'000000', h.hexdigest()):
        print "lowest number is %d" % i
        break
