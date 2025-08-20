import random
import re

# Функции
funcs = {
    #"randint": random.randint,
    "randint": lambda a, b: random.randint(a, b),
    "mod": lambda a, b: a % b,
    "add": lambda a, b: a + b,
    "mul": lambda a, b: a * b,
    "if": lambda cond, a, b: a if cond else b,
}

def split_args(s):
    """Разделяет аргументы по запятым с учётом скобок и строк"""
    args = []
    cur = []
    depth = 0
    in_str = False
    q = None
    i = 0
    while i < len(s):
        ch = s[i]
        if in_str:
            cur.append(ch)
            if ch == q:
                in_str = False
            i += 1
            continue
        if ch in ("'", '"'):
            in_str = True
            q = ch
            cur.append(ch)
            i += 1
            continue
        if ch == '(':
            depth += 1
            cur.append(ch)
            i += 1
            continue
        if ch == ')':
            depth -= 1
            cur.append(ch)
            i += 1
            continue
        if ch == ',' and depth == 0:
            args.append(''.join(cur).strip())
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    if cur:
        args.append(''.join(cur).strip())
    return args

def evaluate(expr):
    """Вычисляет выражение или функцию."""
    if isinstance(expr, (int, float, bool)):
        return expr
    expr = expr.strip()
    if (expr.startswith("'") and expr.endswith("'")) or (expr.startswith('"') and expr.endswith('"')):
        return expr[1:-1]
    # функции
    if expr.startswith('$'):
        expr = expr[1:]
        name = []
        i = 0
        while i < len(expr) and (expr[i].isalnum() or expr[i]=='_'):
            name.append(expr[i])
            i += 1
        name = ''.join(name)
        if i >= len(expr) or expr[i] != '(':
            raise ValueError(expr)
        depth = 0
        j = i
        while j < len(expr):
            if expr[j] == '(':
                depth += 1
            elif expr[j] == ')':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        args_str = expr[i+1:j]
        args = split_args(args_str)
        evaled = [evaluate(a) for a in args]
        if name not in funcs:
            raise ValueError(f"Неизвестная функция {name}")
        if name == "if":
            # специальная обработка: вычисляем все функции в условии
            cond_expr = args[0]  # исходная строка
            cond_evaled = replace_funcs_in_expr(cond_expr)
            cond = eval(cond_evaled, {"__builtins__": None})
            return funcs[name](cond, evaled[1], evaled[2])
        return funcs[name](*evaled)
    else:
        # числа
        try:
            return int(expr)
        except ValueError:
            try:
                return float(expr)
            except ValueError:
                return expr  # оставляем как есть

def replace_funcs_in_expr(expr):
    """Находит все $func(...) в expr и заменяет их на вычисленные значения"""
    pattern = re.compile(r'\$[a-zA-Z_][a-zA-Z0-9_]*\([^()]*\)')
    while True:
        m = pattern.search(expr)
        if not m:
            break
        val = evaluate(m.group())
        expr = expr[:m.start()] + str(val) + expr[m.end():]
    return expr

def parse_string(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == '$':
            start = i
            depth = 0
            i += 1
            while i < len(s):
                if s[i] == '(':
                    depth += 1
                elif s[i] == ')':
                    depth -= 1
                    if depth == 0:
                        i += 1
                        break
                i += 1
            expr = s[start:i]
            val = str(evaluate(expr))
            result.append(val)
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)

# ====== тесты ======
if __name__ == "__main__":
    print(parse_string("$if($randint(10,$add(10, 10)) > 5, 'ok', 'no')"))
    print(parse_string("$if($randint(1,10) > 50, 'ok', 'no')"))
    print(parse_string("$if($mod($randint(1,10),2)==0,'чет','нечет')"))
    print(parse_string("$add($randint(1,5), $mul(2,3))"))
    print(parse_string("$randint(1,5)"))
    print(parse_string("[$add('aaa', 'bbb')]"))

