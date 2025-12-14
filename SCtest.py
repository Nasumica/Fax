import math
import statcalc as SC

SC.sctest()

s = SC.StatCalc("zbir neparnih brojeva")
for x in range(1, 100000, 2): s.Add(x)
s.Report()

s.Reset("test")
s.Report()

n = 100000
for i in range(0, n+1):
    x = i/n/2 * math.pi
    s.Add(math.sin(x))
s.Report()