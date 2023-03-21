def double(func):
	# Function has no arguments. Run, print, run.
	def wrapper_func():
		func()
		print("Let's try that again!")
		func()
	return wrapper_func()
