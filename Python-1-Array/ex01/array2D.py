import numpy

def is_valid_2d_array(family) -> bool:
    if not family:
        print("Error: Array cannot be empty.")
        return False
    first_size = len(family[0])
    for lst in family:
        if not lst:
            print("Error: Lists cannot be empty.")
            return False
        if not isinstance(lst, list):
            print("Error: Array must contain lists.")
            return False
        if not len(lst) == first_size:
            print("Error: Lists must have the same size.")
            return False
    return True

def slice_me(family: list, start: int, end: int) -> list:
    if not (isinstance(start, int) and isinstance(end, int)):
        print("Error: Start and end must be integers.")
        return None
    if not is_valid_2d_array(family):
        return None
    family_array = numpy.array(family)
    print(f"My shape is : {family_array.shape}")
    new_family_array = numpy.array(family[start:end])
    print(f"My new shape is : {new_family_array.shape}")

    return family[start:end]

def main():
    # Tests subject
    family = [[1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    print()

    # Start is not an integer
    print(slice_me(family, "0", -2))
    print()

    # Empty lists
    family = [[2],
            [],
            []]
    slice_me(family, 0, 2)
    print()

    # Lists doesn't have the same size
    family = [[2, 5],
            [2],
            [3, 6]]
    slice_me(family, 0, 2)
    print()

    # Incorrect type in array
    family = [[25],
            2,
            [3]]
    slice_me(family, 0, 2)
    print()

    # Empty array
    family = []
    slice_me(family, 0, 2)
    print()

if __name__ == "__main__":
    main()