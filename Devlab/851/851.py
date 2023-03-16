# https://www.borntodev.com/devlab/task/851

import math

a = [int(i) for i in input().split(',')]
b = [int(i) for i in input().split(',')]

lcm = int(a[1] * b[1] / math.gcd(a[1], b[1]))
new_a0 = a[0] * lcm / a[1]
new_b0 = b[0] * lcm / b[1]

c = int(new_a0 + new_b0)
if c%lcm == 0:
  print(f'{c/lcm:.0f}')
else:
  gcd = math.gcd(c, lcm)
  c /= gcd
  lcm /= gcd
  print(f'{c:.0f}/{lcm:.0f}')
  