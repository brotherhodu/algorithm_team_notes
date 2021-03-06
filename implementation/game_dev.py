# 게임 개발

# 매뉴얼에 따라 캐릭터를 이동 시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

# 입력 조건
# 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3<=N, M<=50)
# 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다. 방향 d의 값으로는 다음과 같이 4가지가 존재한다. 
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
# 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어 있다. 
# 0: 육지, 1: 바다
# 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.

# 출력조건
# 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.


# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# 이 방법은 DP 테이블을 만드는 형태와 유사함
d = [[0]*m for _ in range(n)]

# 현재 캐릭터의 X 좌표, Y 좌표 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global direction # 전역변수를 끌어다 쓰기
  direction -= 1
  if direction == -1:
    direction = 3

# 시뮬레이션 시작
count = 1 # 시작할 때 한 칸 이미 방문했기 때문에 초기값 count = 1
turn_time = 0
while True:
  # 왼쪽으로 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0: # array[nx][ny] == 0 은 육지라는 의미
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0 # turn_time 초기화
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  # 네 방향 모두 갈 수 없는 경우, 뒤로 가기
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time = 0 # 뒤로 이동하게 되면 다시 turn_time = 0 으로 초기화

# 정답 출력
print(count)
