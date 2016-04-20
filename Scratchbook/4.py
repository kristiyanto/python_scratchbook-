#! /bin/usr/python3.5

def main():
    s = "aaaaabbbcc"
    result = compressThis(s)
    print("{}".format(result))
    
def compressThis(s):
    r = list(s[1])
    counter = 0
    for i in range(len(s)):
        c = s[i]
        if r[-1] != c and counter < 2: r.append(c)
        elif r[-1] == c: 
            counter = counter+1
            print(counter)
        else: 
            r.append(counter)
            print("Counter", counter)
            counter = 0
            
    return r
if __name__ =="__main__": main()