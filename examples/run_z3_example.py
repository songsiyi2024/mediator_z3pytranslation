# Minimal Z3 example corresponding to the Counter automaton (k=5)
from z3 import *

k = 5
x = [ Int(f'x_{i}') for i in range(k+1) ]

s = Solver()
# initial
s.add( x[0] == 0 )

for t in range(k):
    # two transitions: (1) x >= 0 -> x = x + 1; (2) x > 5 -> x = x - 10
    g1 = x[t] >= 0
    u1 = x[t+1] == x[t] + 1
    g2 = x[t] > 5
    u2 = x[t+1] == x[t] - 10
    s.add( Or( And(g1, u1), And(g2, u2) ) )

# property: safe: x >= 0  -> look for violation within bound
bad = Or([ x[i] < 0 for i in range(k+1) ])
print('checking for counterexample to safety (x >= 0) up to k=', k)
print(s.check())
if s.check() == sat:
    print('counterexample model:')
    print(s.model())
else:
    print('no counterexample found up to k=', k)
