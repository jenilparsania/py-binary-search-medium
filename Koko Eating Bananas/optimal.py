#  not able to work in leetcode but working in VS code 
import math

def minEatingSpeed(piles, h):
    def totalHours(piles, hourly_rate):
        total = 0
        for i in range(len(piles)):
            total = total + math.ceil(piles[i] / hourly_rate)
        return total

    answer= -1
    high = max(piles)
    low = 0
    while low<=high:
        mid = (low+high)//2
        th = totalHours(piles,mid)
        if th<=h:
            high = mid -1
            answer = mid
        else:
            low = mid + 1
    return answer


piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles,h))