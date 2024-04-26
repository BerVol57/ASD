from collections import deque

d = deque(maxlen=3)

d.append(1)
d.append(12)
d.append(123)
print(d)
d.append(1234)
print(d)
print(d.popleft())
print(d.popleft())
print(d.popleft())
print(d)
