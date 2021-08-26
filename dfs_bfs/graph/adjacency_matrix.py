# 인접 행렬은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식

# 인접 행렬방식 예제

INF = 999999999 # 무한의 비용 선언 (연결되지 않은 노드는 '무한대'로 표현)

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
  [0, 7, 5],
  [7, 0, INF],
  [5, INF, 0]
]

print(graph)