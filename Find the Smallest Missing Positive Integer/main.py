"""
Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.

def findSmallestMissingPositive(orderNumbers):
    # Write your code here

"""


# znaleść najmniejsza dodatnia | ograniczenie czasu i pamięci !

# moje rozwiązanie -> ok 

def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)

    # liczby poza zakresem
    for i in range(n): 
        if orderNumbers[i] <= 0 or orderNumbers[i] > n:
            orderNumbers[i] = n + 1
            
    #       
    for i in range (n):
        x = abs(orderNumbers[i])
        if 1 <= x <= n:
            orderNumbers[x -1] = -abs(orderNumbers[x - 1])
    
    for i in range(n):
        if orderNumbers[i] > 0:
            return i + 1
    
    return n + 1

