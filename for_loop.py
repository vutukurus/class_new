import pdb
#task1: at line 4
#task2: at line 28
#i made some changes
test = "one.py"
#check whether it has extension .py or not..
#for loop
#indeing/sicing
#inbuilt endswith
print "this is hudson demo"
print "this is hudson demo"


'''
test="python"

f=0
for i in test:
	print i
	if i == "t":
		print "found"
		break
print "i am the end"
'''



'''
#Todo: p is repeatedly counted, gate it to print once
test = "ppppythonhhht"
e=0
for i in test:
	e=0
	for j in test:
		#p
		if j == i:
			e=e+1
	print " '%s' is counted %s" %(i,e)
'''			
	





'''
#For loop
test = "python"
#print len(test)
#logic to find len of string..
c=0
for i in "python": 
	print i
	c=c+1 #c=1 #c=2

print "len of test %s"  %c
print "len of test",c

#find method... "t" presence..
d=0
for i in test:
	#pdb.set_trace()
	if i == "t":
		print "found t"
		print "found t at positing %s" %d
	d=d+1
'''

test = 123456  #int 
test=str(test) #str
j=0
for i in test: #str
	j=int(i)+j

print j