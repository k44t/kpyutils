

def backslash_escape(chars, s):
    return ''.join(f'\\{c}' if c in chars else c for c in s)