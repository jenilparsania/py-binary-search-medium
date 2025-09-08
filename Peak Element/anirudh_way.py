def findPeakElement(arr: list) -> int:
    # Write your code here
    #  would try to solve with binary search 
    n=len(arr)
    # for the edges 
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    low = 1
    high = n-2
    while low<=high:
        mid = (low+high)//2
        if arr[mid] > arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low = mid + 1
        else:
            high = mid -1
            

    
    
        

    pass
