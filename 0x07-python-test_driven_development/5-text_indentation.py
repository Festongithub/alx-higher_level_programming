#!/usr/bin/python3

def text_indentation(text):
  """
  Prints a text with 2 new lines after each of these characters: ., ? and :.

  Args:
      text: The text to format.

  Raises:
      TypeError: If text is not a string.
  """

  if not isinstance(text, str):
    raise TypeError("text must be a string")

  # Split the text into words
  words = text.split()

  # Initialize variables
  new_line = False
  for word in words:
    # Check if the word ends with a special character
    if word.endswith((".", "?", ":")):
      # Print the word and two new lines
      print(word + "\n\n", end="")
      new_line = True
    else:
      # Print the word without any new lines
      if new_line:
        print()
      print(word, end=" ")
      new_line = False

  # Print any remaining words
  if not new_line:
    print()
