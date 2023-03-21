import time

def timestamp(func):
	def wrapper_func(*args, **kwargs):
		print(time.ctime())
		return func(*args, **kwargs)
	return wrapper_func
