def lex_precedes(a, b):
    '''
    Compares 2 strings lexicographically, returns True if a < b.
    Uppercase letters come before lowercase.
    '''

    for i in range(min(len(a), len(b))):
        a_ord = ord(a[i])
        b_ord = ord(b[i])
        if (a_ord != b_ord):
            return a_ord < b_ord

    return len(a) < len(b)

a = input()
b = input()

greater = b if lex_precedes(a, b) else a
print(greater)