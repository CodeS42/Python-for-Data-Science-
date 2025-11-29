import sys


def ispunctuation(c):
    punc = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    for sign in punc:
        if c == sign:
            return True

    return False


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) < 2 or not sys.argv[1]:
            string = "Hello World!\r"
            print("What is the text to count?")
            print(string)
        else:
            string = sys.argv[1]

        upp_char = sum(c.isupper() for c in string)
        low_char = sum(c.islower() for c in string)
        punc_char = sum(ispunctuation(c) for c in string)
        digits = sum(c.isdigit() for c in string)
        spaces = sum(c.isspace() for c in string)

        total = upp_char + low_char + punc_char + digits + spaces

        print(f"The text contains {str(total)} characters:")
        print(f"{str(upp_char)} upper letters")
        print(f"{str(low_char)} lower letters")
        print(f"{str(punc_char)} punctuation marks")
        print(f"{str(spaces)} spaces")
        print(f"{str(digits)} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
