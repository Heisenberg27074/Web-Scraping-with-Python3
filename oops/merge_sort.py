def merge_sort(list_a):

    if len(list_a)>1:
        mid=len(list_a)//2
        L=list_a[:mid]
        R=list_a[mid:]
        merge_sort(L)
        merge_sort(R)
        i=0
        j=0
        k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                list_a[k]=L[i]
                i+=1
            else:
                list_a[k]=R[j]
                j+=1
            k+=1
        while i<len(L ):
            list_a[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            list_a[k]=R[j]
            j+=1
            k+=1
list_a=[84,21,96,15,47]
merge_sort(list_a)
print(list_a)
