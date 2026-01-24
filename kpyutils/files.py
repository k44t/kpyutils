import os

def make_parent_dirs(path):
  parent_directory = os.path.dirname(path)

  os.makedirs(parent_directory, exist_ok=True)



def sanitize_filename(filename):
    replacements = {
        '\\': '＼',
        '/': '／',
        ':': '꞉',
        '*': '＊',
        '?': '？',
        '"': '＂',
        '<': '＜',
        '>': '＞',
        '|': '｜',
        '\0': '',  # Remove null character
    }
    return ''.join(replacements.get(c, c) for c in filename)

def unsanitize_filename(sanitized_filename):
    replacements = {
        '＼': '\\',
        '／': '/',
        '꞉': ':',
        '＊': '*',
        '？': '?',
        '＂': '"',
        '＜': '<',
        '＞': '>',
        '｜': '|',
    }
    return ''.join(replacements.get(c, c) for c in sanitized_filename)