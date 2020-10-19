class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        for i in S:
            if i == '#' and len(stack1) != 0:
                stack1.pop()
            else:
                stack1.append(i)
        for i in stack1:
            if i == '#':
                stack1.reverse()
                stack1.pop()
                stack1.reverse()
            
        for j in T:
            if j == '#' and len(stack2) != 0:
                stack2.pop()
            else:
                stack2.append(j)
        for j in stack2:
            if j == '#':
                stack2.reverse()
                stack2.pop()
                stack2.reverse()
        return stack1 == stack2

    
    class Solution:
    
    def putInQueue(self, queue, string):

        for i in string:
            if i == "#":
                if queue:
                    queue.pop()
                else:
                    continue
            else:
                queue.append(i)

        return queue
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        queue0 = deque()
        queue1 = deque()

        queue0 = self.putInQueue(queue0, S)
        queue1 = self.putInQueue(queue1, T)

        if queue0 == queue1:
            return True
        else:
            return False

        
