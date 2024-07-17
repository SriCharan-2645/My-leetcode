"""
919 · Meeting Rooms II
Algorithms
Medium

Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
 find the minimum number of conference rooms required.)

(0,8),(8,10) is not conflict at 8

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2

Input: intervals = [(2,7)]
Output: 1
Explanation:
Only need one meeting room
"""
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        #create a start and end array
        startA , endA = [], []
        for i in intervals:
            startA.append(i.start)
            endA.append(i.end)
        # sort arrays
        startA.sort()
        endA.sort()
        #create 2 pointers
        s1, e1 = 0, 0
        #coutnter
        res, count = 0, 0
        while s1 < len(startA):
            if startA[s1] < endA[e1]:
                count += 1
                s1 += 1
            else:
                count -= 1
                e1 += 1
            res = max(res,count)
        return res
