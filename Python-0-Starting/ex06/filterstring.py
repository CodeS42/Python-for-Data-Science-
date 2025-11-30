import sys
from ft_filter import ft_filter


def valid_arguments(args):
    try:
        int(sys.argv[2])
        str(sys.argv[1])
    except ValueError:
        return False
    return True


def main():
    try:
        if not len(sys.argv) == 3 or not valid_arguments(sys.argv[1:]):
            raise AssertionError("the arguments are bad")
        N = int(sys.argv[2])
        string = str(sys.argv[1])
        S = string.split()
        if not S:
            raise AssertionError("string does not contain any words")
        for elem in S:
            if not elem.isalnum():
                raise AssertionError("string contains forbidden characters")
        print(ft_filter(lambda word: len(word) > N, S))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
