from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        degree=[0]*numCourses
        for course,pre in prerequisites:
            graph[pre].append(course)
            degree[course]+=1
        q=deque()
        for i in range(numCourses):
            if degree[i]==0:
                q.append(i)
        finished=0
        while q:
            course=q.popleft()
            finished+=1
            for n in graph[course]:
                degree[n]-=1
                if degree[n]==0:
                    q.append(n)
        return finished==numCourses