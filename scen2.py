import yaml

yaml_code = """
steps:
  - set_var:
      login_time: "$time(%Y-%m-%d %H:%M:%S)"
  - log: template1.template
  - wait: 2s
  - log: ssh_failed_password.template
  - wait: 1s
  - repeat:
      count: 3
      steps:
        - log: invalid_user.template
        - wait: 1s
"""

data = yaml.safe_load(yaml_code)
commands = data["steps"]

def run(commands):
    # стек: (список_команд, индекс, сколько_раз_повторить)
    stack = [(commands, 0, 1)]

    while stack:
        cmds, i, repeat_left = stack.pop()

        # закончили список → проверим повторы
        if i >= len(cmds):
            if repeat_left > 1:
                stack.append((cmds, 0, repeat_left - 1))
            continue

        cmd = cmds[i]

        if "log" in cmd:
            print("log:", cmd["log"])

        elif "wait" in cmd:
            print("wait:", cmd["wait"])

        elif "set_var" in cmd:
            for k, v in cmd["set_var"].items():
                print("set_var:", k, "=", v)

        elif "repeat" in cmd:
            count = cmd["repeat"]["count"]
            inner_cmds = cmd["repeat"]["steps"]
            # Сначала вернём в стек продолжение после repeat
            stack.append((cmds, i+1, repeat_left))
            # Потом положим вложенные команды
            stack.append((inner_cmds, 0, count))
            continue

        else:
            raise ValueError(f"Неизвестная команда: {cmd}")

        # вернём в стек текущий блок, но сдвинем индекс
        stack.append((cmds, i+1, repeat_left))


# Запуск
run(commands)

