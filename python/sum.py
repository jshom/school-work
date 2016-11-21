import time
sum = 0
go = True
while go:
	num=int(input('enter num: '))
	sum+=num
	go=num!=0
	print 'adding it to the sum. gimme some time'
	time.sleep(2)
print "sum:", sum
