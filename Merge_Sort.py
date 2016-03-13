def  _ItComparator(x ,y):return x>y

def  _ItComparatorDec(x ,y):return x<y


def mergeSort(increasing,price,name, comparator):#add here
    if len(price)>1:
        mid = int(len(price)//2)
        lefthalf = price[:mid]
        righthalf = price[mid:]
        lefthalf2 = name[:mid]
        righthalf2 = name[mid:]
        #add here

        mergeSort(increasing,lefthalf,lefthalf2, comparator)#add here
        mergeSort(increasing,righthalf,righthalf2, comparator)#add here

        i=0
        lefthalfi=0
        righthalfi=0
        lefthalf2i=0
        righthalf2i=0
        while True:
            if lefthalfi>=len(lefthalf):price[i:]=  righthalf[righthalfi:]; break
            if righthalfi >= len(righthalf):price[i:]= lefthalf[lefthalfi:]; break
            if comparator(lefthalf[lefthalfi],righthalf[righthalfi]):
                price[i]=lefthalf[lefthalfi]
                lefthalfi += 1
            else:
                price[i]=righthalf[righthalfi]
                righthalfi+=1
            i+=1
