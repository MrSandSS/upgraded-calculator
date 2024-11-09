print('Type +, -, *, / to perform mathematical operations and type numbers')
print('Type history while selecting a number to get the history')
history = set()
result = 0
first_iteration = True
while True:
    if first_iteration is True:
        print('Type 1st number')
        num1 = int(input())
        print(num1)
        history.add(num1)
        print('Type 2nd number')
        num2 = int(input())
        print(num2)
        print('Type mathematical operation')
        action = input()
        history.add(num2)
        if action == '+':
            result = num1 + num2
            history.add(action)
        elif action == '-':
            result = num1 - num2
            history.add(action)
        elif action == '*':
            result = num1 * num2
            history.add(action)
        elif action == '/':
            result = num1 / num2
            history.add(action)
        print(result)
        first_iteration = False
    elif first_iteration is False:
        print('Type number')
        num = int(input())
        print('Type mathematical operation')
        action = input()
        if action == 'history':
            print(history)
            print("Type mathematical operation (u can't get history now)")
            action = input()
        if action == '+':
            result += num
            history.add(num)
        elif action == '-':
            result -= num
            history.add(num)
        elif action == '*':
            result *= num
            history.add(num)
        elif action == '/':
            result /= num
            history.add(num)
        print(result)