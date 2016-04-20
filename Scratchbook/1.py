#!/usr/bin/python3.5

def main():
    the_string = "abcde"
    result = isUniqueChars(the_string)
    print(result)

def isUniqueChars(the_string):
    if len(the_string) > 128:
        print(len(the_string))
        return False
    else:
        charByte = bytearray()
        for char in the_string:
            print(char, end="\n") if ord(char) in charByte else charByte.append(ord(char))
        return(charByte)

if __name__ == "__main__": main()