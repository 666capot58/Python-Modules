# Module 5

# Problem 1

import random

for i in range(10):
  print(random.randint(25, 35))

  # Problem 2

  import random

  r = random.randint(0, 100)
  while r % 2 == 0:
      r = random.randint(0, 100)

  print(r)

  # Problem 3

  import random

  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  idx = random.randint(0, 6)
  print(days[idx])

  # Problem 4

  from math import pi, acos

  pi_value = 2 * acos(0.0)

  print(pi_value, pi)

# Problem 5
import math


radians = float(input("Enter in radians: "))
print(radians, math.degrees(radians))

# Problem 6
import math

n = int(input("Enter number: "))
fact = 1
temp = n

while temp:
  fact *= temp
  temp -= 1

print(fact, math.factorial(n))