# 재귀함수는 자기 자신을 다시 호출하는 함수
def recursive_function():
  print('재귀함수를 호출합니다.')
  recursive_function()

# recursive_function()

# 재귀함수는 종료 조건을 꼭 명시해야 한다.

# 재귀함수는 함수를 계속 호출했을 때, 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문에 기본적으로 '스택구조'를 가진다.

# 따라서 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀함수로 구현할 수 있다. (ex. DFS)

# 재귀함수 종료 예제
# 재귀 함수를 100번 호출하도록 작성한 코드

def recursive_function(i):
  if i == 100:
    return 
  print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
  recursive_function(i+1)
  print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)