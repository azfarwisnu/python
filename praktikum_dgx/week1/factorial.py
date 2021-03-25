def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
	print(n)


num = 6
print("factorial of",num,"is",factorial(num))
