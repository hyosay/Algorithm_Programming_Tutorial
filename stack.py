def stackin(n):
    stack.append(n)
    return stack

def stackout():
    if len(stack) == -1:
        return stack
    del (stack[len(stack) - 1])
    return print(stack)

stack = []
print(stack)
print(stackin(1))
print(stackin(2))
print(stackin(3))
stackout()
stackout()
stackout()

