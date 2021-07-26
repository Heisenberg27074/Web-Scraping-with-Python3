def bubble(list_a):
    sorted=False
    while not sorted:
        sorted=True
        for i in range(1,len(list_a)):
            if list_a[i-1]>list_a[i]:
                sorted= False
                list_a[i],list_a[i-1]=list_a[i-1],list_a[i]

    return list_a

print(bubble([4,9,6,3,58,7,6,5]))
