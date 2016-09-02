#Lists..
test=["python","perl","jython",[1,2,3,4],6,7]
print test[3][2]
test[3][2] =900
print test



'''
test = ["python","perl",1,2,3,4,5]
a = [10,20,30,40]

#shallow copy
test = a[:] #obj is copied...vallues cop
#test = a #obj is copied...vallues cop
print test
print a
a[0]=90
print test #10,20,30,40
print a #90,20,30,40
'''


'''
print test
print test[0]

test[0]="class"
print test
test[-1]="dummy"
print test
'''
