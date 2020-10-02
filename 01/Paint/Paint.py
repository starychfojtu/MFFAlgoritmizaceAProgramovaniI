def read_int(text):
	while True:
		try:
			return int(input(text))
		except ValueError:
			print('Invalid number.\n')

def read_input():
	return read_int('Width: '), read_int('Length: '), read_int('Height: ')

def calculate_paint_meters(width, length, height):
	return 2 * height * length + 2 * height * width + width * length

# Main

width, length, height = read_input()
meters_required = calculate_paint_meters(width, length, height)
print('You need {0} square meters of paint.'.format(meters_required))
