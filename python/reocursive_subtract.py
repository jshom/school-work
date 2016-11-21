x = int(raw_input("Please enter an integer: "))
def printDownToZero(num):
    if num == 0:
        return
    print num
    printDownToZero(num-1)
printDownToZero(x)
