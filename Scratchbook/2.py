#! /usr/bin/python3.5
# Check if string is Permutation

def main():
    str1 = "TacO Bell"
    str2 = "lleB ocaT"
    
    result = isPermutation(str1,str2)
    print("{}".format(result))
    
def isPermutation(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        return "".join(sorted(str1.lower())) == "".join(sorted(str2.lower()))

if __name__ == "__main__": main()