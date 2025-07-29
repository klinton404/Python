from collections import deque

name= deque(["klinton","Newton","Tusen"])
print(name)


name.popleft()
print(name)

name.popleft()
name.popleft()
if not name:
    print("No person left")
