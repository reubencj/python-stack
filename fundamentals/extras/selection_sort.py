
arr = [78,70,325,34,21,100]


def selection_sort(ls):
    for j in range(len(ls)-1):
       
        minIndex = j
        
        for x in range(j+1, len(ls)):
            
            if ls[minIndex] > ls[x]:
                minIndex = x

        if minIndex != j:
            ls[j], ls[minIndex] = ls[minIndex], ls[j]
        
    print(f"result is {ls}")


selection_sort(arr)