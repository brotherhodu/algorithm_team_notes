# stack은 박스쌓기
# 선입후출 후입선출 구조

a = [1, 2, 3, 4, 5]
a.append(6)
print(a)

a.pop()
print(a)

# 파이썬에서 stack은 별도의 라이브러리가 필요없다.
# 기본 리스트에서 append()와 pop() 메서드를 사용한다.

# stack example
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력