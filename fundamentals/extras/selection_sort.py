
arr = [78,70,325,34,21,100]


def selection_sort(ls):
    #first iternate through all whole list, stop before the second last index to not go over the bound of the list
    for j in range(len(ls)-1):
       
       #set the min index to the starting index by default
        minIndex = j
        
        #iterate through next index to the end of the list
        for x in range(j+1, len(ls)):
            
            #if the value if less than the value in minIndex then store the index
            if ls[minIndex] > ls[x]:
                minIndex = x

        #if the minIndex is not the same as the iterated value then swap 
        if minIndex != j:
            ls[j], ls[minIndex] = ls[minIndex], ls[j]
        
    print(f"result is {ls}")


selection_sort(arr)