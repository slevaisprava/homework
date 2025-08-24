commands = ["log", "wait","repeat","count","2","log1","wait","end","wait","log"]

def run(commands):
    stack = []  # стек блоков repeat
    i = 0
    while i < len(commands):
        cmd = commands[i]
        print(stack)
        if cmd == "log":
            print("log")
            i += 1
        
        elif cmd == "log1":
            print("log1")
            i += 1
        elif cmd == "wait":
            print("wait")
            i += 1

        elif cmd == "repeat":
            if i+2 >= len(commands) or commands[i+1] != "count":
                raise ValueError("После repeat должна идти команда 'count' и число")
            count = int(commands[i+2])
            stack.append((i+3, count))
            i = i+3

        elif cmd == "end":
            start, count = stack[-1]
            if count > 1:
                stack[-1] = (start, count-1)
                i = start
            else:
                stack.pop()
                i += 1
        else:
            raise ValueError(f"Неизвестная команда: {cmd}")

# Прогон 2 раза всего списка
for _ in range(2):
    run(commands)

