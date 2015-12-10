from itertools import groupby
step = "1113122113"
for i in range(50):
    p = [list(g) for k, g in groupby(step)]
    step = "".join(["%d%s" % (len(l), l[0]) for l in p])
    if i == 39:
        print "part 1.  length= %d " % (len(step))

print "part 2.  length= %d " % (len(step))

##                              A N S W E R S
##  part 1.  length= 360154
##  part 2.  length= 5103798
