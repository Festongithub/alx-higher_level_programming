#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
  """
  Prints x elements of a list.

  Args:
      my_list: The list to print elements from.
      x: The number of elements to print.

  Returns:
      The number of elements actually printed.
  """

  try:
    count = 0
    for i in range(x):
      print(my_list[i], end=" ")
      count += 1
  except IndexError:
    for element in my_list:
      print(element, end=" ")
      count += 1
  print()
  return count
