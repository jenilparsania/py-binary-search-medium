def shipWithinDays(weights:list,days:int):
    final_answer = 0
    
    def daysCalculator(weights:list,bags:int):
        expectedDays = 1    # making this into 1 from 0
        total = 0
        for i in range(0,len(weights)):
            total += weights[i]

            if total > bags:
                total = total - weights[i]
                expectedDays += 1
                total = weights[i]  # wrote this from total = 0
            
        return expectedDays
    
    high = sum(weights)
    low = max(weights)

    while low<=high:
        mid = (low+high)//2
        expectedDays = daysCalculator(weights,mid)
        if expectedDays <= days:
            final_answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return final_answer

        

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5 

print(shipWithinDays(weights,days))  # expected Output : 15
print(shipWithinDays([3,2,2,4,1,4],3)) # expected Output : 6