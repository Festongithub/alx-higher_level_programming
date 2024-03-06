#!/usr/bin/python3

def matrix_divided(matrix, div):
  """
  Divides all elements of a matrix by a divisor.

  Args:
      matrix: A 2D list of numbers.
      div: The number to divide each element by.

  Raises:
      TypeError: If the matrix is not a list of lists, or if any element in the matrix is not an integer or float.
      TypeError: If each row of the matrix is not of the same size.

  Returns:
      A new 2D list with all elements divided by the divisor.
  """

  # Check if matrix is a list of lists
  if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

  # Check if each row is of the same size
  if not all(len(row) == len(matrix[0]) for row in matrix):
    raise TypeError("Each row of the matrix must be of the same size")

  # Check if all elements are integers or floats
  if not all(isinstance(element, (int, float)) for row in matrix for element in row):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

  # Check if divisor is zero
  if div == 0:
    raise ValueError("div must not be 0")

  # Create a new matrix to store the results
  result = []

  # Iterate over each row in the matrix
  for row in matrix:
    # Create a new row to store the divided elements
    new_row = []

    # Iterate over each element in the row
    for element in row:
      # Divide the element by the divisor and append it to the new row
      new_row.append(element / div)

    # Append the new row to the result matrix
    result.append(new_row)

  # Return the result matrix
  return result
