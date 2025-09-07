"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with 
packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt
 being shipped within days days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting 
the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

"""
def shipWithinDays(weights:list,days:int):
    

    
    
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
    
    maxi = 2* max(weights) 

    for i in range(0,maxi):
        sample_days = daysCalculator(weights,i)

        if sample_days <= days:
            return i
        

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5 

print(shipWithinDays(weights,days))  # expected Output : 15
print(shipWithinDays([3,2,2,4,1,4],3)) # expected Output : 6
        
    

