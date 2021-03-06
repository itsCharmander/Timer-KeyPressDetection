import sys, time, msvcrt



def readInput( caption, default, timeout = 5):

    start_time = time.time()
    sys.stdout.write('%s(%s):'%(caption, default))
    sys.stdout.flush()
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13: # enter_key
                break
            elif ord(byte_arr) >= 32: #space_char
                input += "".join(map(chr,byte_arr))
        if len(input) == 0 and (time.time() - start_time) > timeout:
            print("timing out, using default value.")
            break

    print('')  # needed to move to next line
    if len(input) > 0:
        return input
    else:
        return default

# and some examples of usage
ans = readInput('Please type a name', 'john') 
print( 'The name is %s' % ans)
ans = readInput('Please enter a number', 10 ) 
print( 'The number is %s' % ans) 