import string

def is_number(c):
    numbers = [str(i) for i in range(10)]
    return c in numbers

def is_letter(c):
    return c in string.ascii_lowercase or c in string.ascii_uppercase

def passwordNormalization(password):
    pw = password
    numbers = []
    letters = []
    other = []
    for c in pw:
        if is_letter(c):
            letters.append(c)
        elif is_number(c):
            numbers.append(c)
        else:
            other.append(c)
    return ''.join(letters+numbers+other)

assert is_number('3')
assert is_letter('d')
assert is_letter('O')
assert passwordNormalization("3A12^,^b4") == "Ab3124^,^"