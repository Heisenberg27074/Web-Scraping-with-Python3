def selection_sort(list_a):
    for i in range(len(list_a)-1):
        min_pos=i
        for j in range(i+1,len(list_a)-1):
            if list_a[min_pos]>list_a[j]:
                min_pos=j
        if min_pos!=i:
            list_a[min_pos],list_a[i]=list_a[i],list_a[min_pos]
    return list_a

print(selection_sort([5,6,3,2,1,4,7,8,9,8,9,7,5,32]))
