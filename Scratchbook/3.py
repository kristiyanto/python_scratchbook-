#! /usr/bin/python3.5
# Check if two strings are one edit away

def main():
    str1 = "thisssss"
    str2 = "thiSssss"
    result = isOneEditAway(str1,str2)
    print("Result is {}".format(result))

def isOneEditAway(str1,str2):
    if len(str1)==len(str2):
        return oneEditReplace(str1, str2)
    elif (len(str1)+1) == len(str2):
        return oneEditInsert(str1,str2)
    elif (len(str1) == (len(str2)+1)):
        return oneEditInsert(str2,str1)
    else:
        return False
    
def oneEditReplace(str1, str2):
    diff = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff += 1
            if diff > 1:
                return False
    return True

def oneEditInsert(str1,str2):
    i1 = 0
    i2 = 0
    while(i1 < len(str1) and i2 < len(str2)):
        if str1[i1] != str2[i2]:
            if (i1 != i2) : return False
            i2 += 2
        else:
            i1 += 1
            i2 += 1
    return True 

if __name__ == "__main__": main()