def sum_to(n):
  return n * (n+1) // 2

# print(sum_to(6))
# print(sum_to(10))


def largest(args):
  large = 0
  for arg in args:
    if arg > large:
      large = arg
  return large

# print(largest([1, 2, 3, 4, 0]))
# print(largest([10, 4, 2, 231, 91, 54]))


def occurrences(str1, str2):
  return str1.count(str2)

# print(occurrences('fleep floop', 'e'))
# print(occurrences('fleep floop', 'p')) 
# print(occurrences('fleep floop', 'ee'))
# print(occurrences('fleep floop', 'fe')) 


def product(*args):
  product = 1
  for arg in args:
    product *= arg 
  return product

# print(product(-1, 4)) 
# print(product(2, 5, 5)) 
# print(product(4, 0.5, 5))