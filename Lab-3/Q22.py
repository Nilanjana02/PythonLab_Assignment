#  Write a Python program to implement stack using array.means you have to write a class named Stack with the following methods: push, pop, isEmpty, isFull, peek, display.

def push(stack, element):
    if isFull(stack):
        print('Stack is full')
    else:
        stack.append(element)
        print(f'{element} pushed into the stack')

def pop(stack):
    if isEmpty(stack):
        print('Stack is empty')
    else:
        print(f'{stack.pop()} popped from the stack')

def isEmpty(stack):
    return len(stack) == 0

def isFull(stack):
    return len(stack) == 10

def peek(stack):
    if isEmpty(stack):
        print('Stack is empty')
    else:
        print(f'Top element is {stack[-1]}')

def display(stack):
    if isEmpty(stack):
        print('Stack is empty')
    else:
        print('Stack elements are:')
        for i in stack:
            print(i)

stack = []
while True:
    print('1. Push')
    print('2. Pop')
    print('3. Is Empty')
    print('4. Is Full')
    print('5. Peek')
    print('6. Display')
    print('7. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        element = int(input('Enter the element: '))
        push(stack, element)
    elif choice == 2:
        pop(stack)
    elif choice == 3:
        print(isEmpty(stack))
    elif choice == 4:
        print(isFull(stack))
    elif choice == 5:
        peek(stack)
    elif choice == 6:
        display(stack)
    elif choice == 7:
        break
    else:
        print('Invalid choice')
    