# Queue는 대기줄이라고 생각하면 된다.
# '공정한' 자료구조. 먼저 들어왔으면 먼저 나간다.
# 선입선출 구조

# 파이썬에서 Queue는 collections 모듈에서 제공하는 deque 자료구조 라이브러리를 활용한다.

# queue example
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)