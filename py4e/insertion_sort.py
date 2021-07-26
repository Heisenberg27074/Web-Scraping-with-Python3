def insertion_sort(list_a):
    index_value=range(1,len(list_a))

    for i in (index_value):
        #value_to_sort=list_a[i]

        while list_a[i-1]>list_a[i] and i>0:
            list_a[i],list_a[i-1]=list_a[i-1],list_a[i]
            i=i-1
    return list_a

print(insertion_sort([6,6544,8,8,6,2,5,8,1,90,]))
