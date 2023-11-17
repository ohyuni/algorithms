import sys

stack = []

def push(x):
    stack.append(x)

def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if not stack:
        print(1)
    else:
        print(0)
    
def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

n = int(input())
commands = [sys.stdin.readline().rstrip() for _ in range(n)]

for command in commands:
    command = command.split(' ')
    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "top":
        top()