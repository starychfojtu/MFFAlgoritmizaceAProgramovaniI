def read_int(text):
	while True:
		try:
			return int(input(text))
		except ValueError:
			print("Invalid number.\n")

def read_input():
	return read_int("X: "), read_int("Y: ")

def try_divide(x, y):
	if x % y == 0:
		return x // y
	else:
		return None

def result_to_string(x, y, result):
	if result is None:
		return "indivisible"
	else:
		return "{0} divided by {1} is {2}".format(x, y, result)

#def try_divide(x, y):
#	return x // y if x % y == 0 else None

# Main

x, y = read_input()
result = try_divide(x, y)
print(result_to_string(x, y, result))

