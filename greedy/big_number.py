# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
list(map(int, input().split()))

# 큰 수의 법칙

# 1. 단순하게 푸는 방법
## N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
## N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1]  # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수 

result = 0

while True:
  for i in range(k): # 가장 큰 수를 K번 더하기
    if m == 0: # m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1 # 더할 때마다 1씩 빼기
  if m == 0: # m이 0이라면 반복문 탈출
    break
  result += second # 두 번째로 큰 수를 한 번 더하기
  m -= 1 # 더할 때마다 1씩 빼기

print(result)  # 최종 답안 출력


# 2. 답안 예시
## N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
## N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받는 수 정렬
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k # 세트로 생각
count += m%(k+1) # 나눠지고 나머지는 모두 가장 큰 수

result = 0
result += (count)*first
result += (m-count)*second

print(result)