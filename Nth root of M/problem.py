"""
Problem statement
You are given two positive integers 'n' and 'm'. You have to return the 'nth' root of 'm', i.e. 'm(1/n)'. If the 'nth root is not an integer, return -1.



Note:
'nth' root of an integer 'm' is a number, which, when raised to the power 'n', gives 'm' as a result.


Example:
Input: ‘n’ = 3, ‘m’ = 27

Output: 3

Explanation: 
3rd Root of 27 is 3, as (3)^3 equals 27.
"""
def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    low = 0
    high = m
    while low<=high:
        mid = (low+high)//2
        if mid **n==m:
            return mid
        if mid **n >m:
            high = mid -1
        else:
            low = mid + 1

    return -1
