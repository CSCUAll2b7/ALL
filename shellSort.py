name = ['a','b','c','d','e','f']
price =[10,8,6,4,2,0]
def shellSort(price, name):
    inc = len(price) // 2
    while inc:
        for i in range(len(price)):
            j = i
            temp = price[i]
            temp2= name[i]
            #add here if need to be sorted
            while j >= inc and price[j-inc] > temp:
                price[j] = price[j - inc]
                name[j] = name[j- inc]
                #add here if need to be sorted
                j -= inc
            price[j] = temp
            name[j] = temp2
            #add here if need to be sorted
        inc = inc//2 if inc//2 else (0 if inc==1 else 1)
shellSort(price,name)
print(name)
print(price)
