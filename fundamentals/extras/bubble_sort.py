arr = [145,133, 100, 70, 0]


def bubble_sort(unsortedList):
    listIter = len(unsortedList)
    for j in range(listIter):

        for x in range(listIter-1-j):
            if unsortedList[x] > unsortedList[x + 1]:
                unsortedList[x], unsortedList[x+1] = unsortedList[x+1], unsortedList[x]
            print(unsortedList)
        
        print(f"j is {j}")

        


bubble_sort(arr)