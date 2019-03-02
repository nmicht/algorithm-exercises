# SOLVED
# https://www.interviewbit.com/problems/merge-overlapping-intervals/
# https://leetcode.com/problems/merge-intervals/submissions/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
        solution = []
        size = len(intervals)

        if size == 0:
            return solution

        intervals.sort(key=lambda x: x.start, reverse=False)

        solution.append(intervals[0])

        for i in range(1, size):
            if intervals[i].start <= solution[-1].end:
                if solution[-1].end < intervals[i].end:
                    solution[-1].end = intervals[i].end
            else:
                solution.append(intervals[i])

        return solution

x = Solution()
print(x.merge([1, 3], [2, 6], [8, 10], [15, 18]))
