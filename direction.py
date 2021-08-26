# 일반적으로 방향을 설정해서 이동하는 문제에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적 (1번 방법!)


# 1) 2차원 리스트로 설정하기
# 동 북 서 남
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 후의 좌표 설정
plans = input().split()
x, y = 1, 1
for plan in palns:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x, y = nx, ny

# 2) 방향벡터로 설정하기
# 가능한 방향벡터를 모두 list로 묶고 변수로 선언
steps = [(-2, -1), (-1,-2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
