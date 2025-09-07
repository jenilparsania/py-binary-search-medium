import math
def smallestDivisor(nums,threshold):

    def answer(nums,divisor):
        total = 0
        for i in range(0,len(nums)):
            total += math.ceil(nums[i]/divisor)
        return total
    
    low = 1
    high = max(nums)

    while low<=high:
        mid = (low+high)//2

        compare = answer(nums,mid)

        if compare<=threshold:
            final = mid  # saving the mid value , which has the possibility to be the answer
            high = mid -1
        else:
            low = mid + 1  

    return final # answer would always be on the low    



nums = [1,2,5,9]
threshold = 6

print(smallestDivisor(nums,threshold))
print(smallestDivisor([44,22,33,11,1],5))