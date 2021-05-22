myList1 = [ range(15)] #it will only print range[0,15)
myList2 = [*range(0, 15)] #but it will print 0 to 15 if u add * on front
myList3 = [*range(4, 15, 3)]
print(myList1)
print(myList2)
print(myList3)
