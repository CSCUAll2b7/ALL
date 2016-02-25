#QUICK SORT ALGORITHM

def quickSort(alist, name):#add here
   quickSortHelper(alist,0,len(alist)-1, name)#add here

def quickSortHelper(alist,first,last, name):#add here
   if first<last:

       splitpoint = partition(alist,first,last, name)#add here

       quickSortHelper(alist,first,splitpoint-1, name)#add here
       quickSortHelper(alist,splitpoint+1,last, name)#add here


def partition(alist,first,last,name):#add here
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark >= rightmark and alist[leftmark] >= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] <= pivotvalue and rightmark <= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
           temp2 = name[leftmark]
           name[leftmark] = name[rightmark]
           name[rightmark] = temp2
           #add here

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   temp2 = name[first]
   name[first] = name[rightmark]
   name[rightmark] = temp2
   #add here


   return rightmark

numbers = [1, 4, 6, 7, 5, 10, 9, 3]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
quickSort(numbers, letters)
print(numbers)
