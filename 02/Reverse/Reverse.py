def reverse(s):
    return s[::-1]

# Solution using explicit slice object.
def reverse_explicit(s):
    reverse_slice = slice(None, None, -1)
    return s[reverse_slice]

print(reverse(input()))
