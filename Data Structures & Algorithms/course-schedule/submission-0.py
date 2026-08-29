from collections import defaultdict as df, deque as dq
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree_counts = df(int)
        adj_list = df(list)
        for s, d in prerequisites:
            indegree_counts[d] += 1
            adj_list[s].append(d)
        next_courses = [i for i in range(numCourses) if indegree_counts[i] == 0]
        courses_taken = 0
        while next_courses:
            courses_taken += 1
            c = next_courses.pop()
            for n in adj_list[c]:
                indegree_counts[n] -= 1
                if indegree_counts[n] == 0:
                    next_courses.append(n)
        return courses_taken == numCourses