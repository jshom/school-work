#!/usr/bin/python
'''
---1--- = 3 : 1
--111-- = 2 : 3
-11111- = 1 : 5
1111111 = 0 : 7

------1
-----111
----11111
---1111111
--111111111
-11111111111
1111111111111
'''
symbol = raw_input('enter a symbol: ')
def makePyramid(height):
    # Damn that sounds like english
    # Set up the initital pyramid
    # ---------------------------
    # First create string of max white space
    if len(symbol) != 1:
        return
    if int(height) < 0:
        return
    height-=4
    white_symbol = ' '
    white_space = white_symbol
    # Then init content
    content = symbol
    # ---------------------------
    # Now fill up the white space
    # it will subtract -1 down
    # The content will add 2 of itself each iteration
    white_counter = 0
    while white_counter <= height:
        white_space+=white_symbol
        white_counter+=1
    # Now the white space is the same count as the height
    layer_count = 0
    # do the first line
    print white_space + white_symbol + symbol
    # then do the rest
    while layer_count <= height + 2:
        content += symbol*2
        print white_space[layer_count:] + content
        layer_count+=1

while True:
        makePyramid(input('\nenter an odd integer for height to: \nSEE THE MAGICAL TRIANGLE APPEAR \n'))
