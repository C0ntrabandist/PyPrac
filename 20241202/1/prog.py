import sys
data = input().encode()
n, tail = data[0], data[1:]
parts = sorted(tail[i * len(tail) // n:(i + 1) * len(tail) // n] for i in range(n))
sys.stdout.buffer.write(bytes([n]) + b''.join(parts))
