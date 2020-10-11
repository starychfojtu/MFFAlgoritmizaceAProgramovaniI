cap_a_ord = ord("A")
low_a_ord = ord("a")
low_z_ord = ord("z")

capital_difference = cap_a_ord - low_a_ord

def is_lower_alpha(c):
    return low_a_ord <= ord(c) <= low_z_ord

def capitalize(c):
    return chr(ord(c) + capital_difference) if is_lower_alpha(c) else c

def to_upper(s):
    return ''.join(capitalize(c) for c in s)

print(to_upper(input()))
