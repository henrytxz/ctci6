def palindrome_permutated(str):
    chars = dict()
    for c in str:
        if c not in ' ,.!?':
            chars[c] = chars.setdefault(c, 0)+1
    num_chars_occur_odd_number_times = 0
    for c, count in chars.iteritems():
        if count%2 == 1:
            num_chars_occur_odd_number_times += 1
    if num_chars_occur_odd_number_times > 1:
        return False
    else:
        return True

if __name__ == '__main__':
    assert palindrome_permutated('abba')
    assert palindrome_permutated('abaaba')
    assert not palindrome_permutated('abca')
    assert palindrome_permutated('tact coa')