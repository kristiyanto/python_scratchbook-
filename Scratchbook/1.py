#!/usr/bin/python3.5
# Check if a string have unique chars

def main():
    the_string = "Hello it's me."
    result = isUniqueChars(the_string)
    print("\n{}".format(result))

def isUniqueChars(the_string):
    for char in the_string:
        the_string = the_string.lstrip(char)
        if char in the_string:
            return False
    return True
if __name__ == "__main__": main()