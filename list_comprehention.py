# 리스트 컴프리헨션 (list comprehension)

# 2차원 리스트 초기화에 효과적이다.
# 리스트 컴프리헨션은 리스트를 초기화하는 방법이다.

# [] 안에 조건문과 반복문을 넣어서 초기화 한다.

# ex. 0부터 19까지의 수 중 홀수만 포함하는 리스트
# 1) 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 2) canonical
array = []
for i in range(20):
  if i % 2 == 1:
    array.append(i)

print(array)

## 리스트 컴프리헨션이 훨씬 간단함!