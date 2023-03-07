# https://www.borntodev.com/devlab/task/813

import math

s = ''.join(sorted(input())).replace('eee', '.')
count_alphabet = [s.count(chr(i)) for i in range(97, 123)]
product_of_factorial = 1
for c in count_alphabet:
  product_of_factorial *= math.factorial(c)
number_of_permutation = math.factorial(len(s)) / product_of_factorial
print(int(number_of_permutation))

