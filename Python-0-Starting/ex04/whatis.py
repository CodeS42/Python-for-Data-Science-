import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("AssertionError: more than one argument is provided")
    elif len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("AssertionError: argument is not an integer")
        if number % 2 == 0:
            print("I'm Even.")
        else :
            print("I'm Odd.")
except AssertionError as e:
    print(e)
