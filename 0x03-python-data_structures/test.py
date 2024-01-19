def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a or tuple_b is smaller than 2, use 0 for missing integers
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    # Use only the first 2 integers if a tuple is bigger than 2
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result

# Example usage
tuple1 = (1, 2)
tuple2 = (3, 4)
result = add_tuple(tuple1, tuple2)
print(result)  # Output: (4, 6)

