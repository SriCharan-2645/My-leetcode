"""
920 · Meeting Rooms
Algorithms
Easy

Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.


(0,8),(8,10) is not conflict at 8

Example

Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation:
Two times will not conflict
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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        #sorting interval objects based on start time
        intervals.sort(key = lambda  i : i.start)

        for i in range(1,len(intervals)): # we are starting from index 1, becasue we also want to check at position 0
            I1 = intervals[i-1] # previous interval
            I2 = intervals[i] # current interval
            if I1.end > I2.start:
                return False
        return True
