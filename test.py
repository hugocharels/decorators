from cache import *
from timer import *

@cache
def fibo(x):
	return x if x in {0, 1} else fibo(x-1) + fibo(x-2)

for i in range(100, 1100, 100):
	@timer(f"test {i}")
	def call_fibo(x):
		ret = fibo(x)
		return ret
	call_fibo(i)

