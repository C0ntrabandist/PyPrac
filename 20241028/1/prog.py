
def fib(m, n):
	a, b = 0, 1
	for i in range(m):
		a, b = b, a + b
	for i in range(n):
		yield b
		a, b = b, a + b

import sys
exec(sys.stdin.read())