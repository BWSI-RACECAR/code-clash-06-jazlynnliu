"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #6 - Longest Distance Between Checkpoints (checkpoints.py)


Author: Chris Lai

Difficulty Level: 3/10

Prompt: The Grand Prix is an obstacle course for the RACECAR. Each of the RACECARs must traverse the course 
and navigate through checkpoints. At the beginning of each obstacle, there will be a checkpoint, at which the 
RACECAR can stop to refuel. Before the course starts, each competitor is given an array of values that indicate 
the distance of these checkpoints (in meters) relative to the starting line. In order to prepare your RACECAR 
for the final race, you want to calculate the longest distance between two checkpoints such that your car has 
enough fuel to last the entire leg.

Given an array of checkpoint distance values, return an integer to represent the longest distance between two checkpoints.

Constraints: All numbers in the array “n” will be integers 10^9 >= n >= 0. Assume the number of items in the 
array “k” will be 10^9 >= k > 0. You may not use the Python sort() method.

Test Cases:
Input: [0, 3, 4, 9] ; Output: 5
Input: [10, 8, 4, 1] ; Output: 4
Input: [5, 0, 3, 6] ; Output: 3
"""

class Solution:
    def longestdistance(self, checkpoints):
        # type checkpoints: list
        # return type: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        newList = []
        minVal = checkpoints[0]
        while len(checkpoints) > 1:
            for x in checkpoints:
                if x < minVal:
                    minVal = x
            newList.append(checkpoints.pop(checkpoints.index(minVal)))
            minVal = checkpoints[0]
        else:
            newList.append(checkpoints[0])
        
        maxdist = newList[1] - newList[0]
        for y in range(len(newList) - 1):
            if (newList[y + 1] - newList [y]) > maxdist:
                maxdist = newList[y + 1] - newList [y]
        
        return maxdist

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.longestdistance(array)
    print(ans)

if __name__ and "__main__":
    main()