# 데이터의 개수 입력
n = int(input())

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 각 데이터를 공백을 구분하여 입력
list(map(int, input().split()))

# python에서 입력의 갯수가 많으면 input()을 사용하면 안된다.
# 데이터 갯수가 N>=10,000,000 이면 input()으로 하면 시간초과
# sys 라이브러리의 readline() 함수 이용
import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
print(input_data)
# sys 라이브러리 사용할 때는 한 줄 입력받고 나서 rstrip() 함수를 꼭 호출해야 readline() 입력 후 엔터가 줄 바꿈 기호로 입력되지 않고 공백 문자를 제거할 수 있다. 

# 2차원의 전체 맵 정보를 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))
