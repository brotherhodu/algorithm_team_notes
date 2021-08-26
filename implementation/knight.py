# 나이트는 말을 타고 있기 때문에 이동을 할 때 L자로 이동을 함 
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
#2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

# 8X8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.

# 현재의 나이트 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int (ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1,-2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
    result += 1

print(result)