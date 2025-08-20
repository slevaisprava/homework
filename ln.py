import math

T = 10.0      # длительность процесса (секунды)
f0 = 10.0      # начальная частота (событий/с)
f1 = 1.0     # конечная частота (событий/с)

# f(t) = f0 + (f1 - f0) * t/T
# N(t) = f0*t + (f1 - f0)/(2*T) * t^2

a = (f1 - f0) / (2 * T)
b = f0
N_total = int(round(f0 * T + (f1 - f0) * T / 2))  # всего событий (55)

times = []
for k in range(1, N_total + 1):
    t = (-b + math.sqrt(b*b + 4*a*k)) / (2*a)
    times.append(t)

# теперь считаем дельты
deltas = [0.0]  # у первого события смещение 0
for i in range(1, len(times)):
    deltas.append(times[i] - times[i-1])

# вывод
n=1
for d in times:
    print(n, f"{d:.6f}")
    n+=1
