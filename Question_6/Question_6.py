while True:

    length=(input())
    if length=="":
        break
    needle=input()
    haystack=input()
    count=0
    if len(haystack)>int(length) and needle in haystack:
        for i in range (0,len(haystack)+1-int(length)):
            for j in range (i,len(haystack)):
                if haystack[i:j+1]==needle:
                    print(i)
    else:
        print("")
        print("")    