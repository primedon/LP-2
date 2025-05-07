def selection_sort(a):
    for i in range (len(a)-1):
        min_index=i
        for j in range (i,len(a)):
            if a[min_index]>a[j]:
                min_index=j

        a[i],a[min_index]=a[min_index],a[i]

a=[1,3,51,2,60]
selection_sort(a)
print("SOrted array is",a)