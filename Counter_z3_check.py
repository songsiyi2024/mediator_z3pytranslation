from z3 import *

x_0 = Int('x_0')

x_1 = Int('x_1')

x_2 = Int('x_2')

x_3 = Int('x_3')

x_4 = Int('x_4')

x_5 = Int('x_5')

x_6 = Int('x_6')

x_7 = Int('x_7')

x_8 = Int('x_8')

x_9 = Int('x_9')

x_10 = Int('x_10')

s = Solver()
s.add(x_0 == 0)

s.add(Or(And(0, x_1 == (x_0 + 1)), And(0, x_1 == (x_0 - 10)))
)

s.add(Or(And(0, x_2 == (x_1 + 1)), And(0, x_2 == (x_1 - 10)))
)

s.add(Or(And(0, x_3 == (x_2 + 1)), And(0, x_3 == (x_2 - 10)))
)

s.add(Or(And(0, x_4 == (x_3 + 1)), And(0, x_4 == (x_3 - 10)))
)

s.add(Or(And(0, x_5 == (x_4 + 1)), And(0, x_5 == (x_4 - 10)))
)

s.add(Or(And(0, x_6 == (x_5 + 1)), And(0, x_6 == (x_5 - 10)))
)

s.add(Or(And(0, x_7 == (x_6 + 1)), And(0, x_7 == (x_6 - 10)))
)

s.add(Or(And(0, x_8 == (x_7 + 1)), And(0, x_8 == (x_7 - 10)))
)

s.add(Or(And(0, x_9 == (x_8 + 1)), And(0, x_9 == (x_8 - 10)))
)

s.add(Or(And(0, x_10 == (x_9 + 1)), And(0, x_10 == (x_9 - 10)))
)

print(s.check())
if s.check() == sat:
    m = s.model()
    print("counterexample model:")
    print(m)
