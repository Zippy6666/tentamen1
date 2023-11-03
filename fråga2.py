def divisible_by_3( string ):
    if not string.isdecimal():
        print("felinmatat")
        return
    
    sum = 0
    for i in string:
        sum += int(i)
    
    return sum%3==0


def divisible_by_4( string ):
    if not string.isdecimal():
        print("felinmatat")
        return
    
    lastChar = string[ len(string)-1 ]
    charBeforeLastChar = string[ len(string)-2 ]
    
    return int(charBeforeLastChar+lastChar) % 4 == 0
        

def divisible_by_11( string ):
    if not string.isdecimal():
        print("felinmatat")
        return
    
    sum = 0
    doMinus = False

    for i in string:
        if doMinus:
            #print("minus", int(i))
            sum -= int(i)
        else:
            #print("plus", int(i))
            sum += int(i)

        doMinus = not doMinus
    
    return sum%11==0

def main():
    
    print( divisible_by_3("132") )
    print( divisible_by_4("132") )
    print( divisible_by_11("132") )




if __name__ == "__main__":
    main()