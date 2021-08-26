# 인접 리스트 방식
# 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
# 연결리스트 라는 자료구조를 이용해 구현한다. 단순히 2차원 리스트를 사용해 구현하면 된다!

# 인접 리스트 방식 예제

# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장 (노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장 (노드, 거리)
graph[2].append((0, 5))

print(graph)