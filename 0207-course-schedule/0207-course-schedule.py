from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        
        graph = [[] for _ in range(numCourses)]

       
        indegree = [0] * numCourses

        
        for course, prerequisiteCourse in prerequisites:
            graph[prerequisiteCourse].append(course)
            indegree[course] += 1

        
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        
        completedCourses = 0

        while queue:
            currentCourse = queue.popleft()
            completedCourses += 1

            
            for nextCourse in graph[currentCourse]:
                indegree[nextCourse] -= 1

                
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        
        return completedCourses == numCourses