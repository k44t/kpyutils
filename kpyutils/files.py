import os
import re
import importlib
import sys

def make_parent_dirs(path):
  parent_directory = os.path.dirname(path)
  os.makedirs(parent_directory, exist_ok=True)


def add_pre_suffix(path, suffix):
   name, ext = os.path.splitext(path)
   return f'{name}{os.path.extsep}{suffix}{os.path.extsep}{ext}'


def list_subdirs(path):
   return [x for x in os.listdir(path) if os.path.isdir(x)]

def load_module_from_file(path):
  module_name = path.replace(os.sep, '.')
  module_name = re.sub(r'\.(\d)', r'._\1', module_name)  # Prefix digits after dots with an underscore
  module_name = re.sub(r'\W|^(?=\d)', '_', module_name)  # Replace non-word characters and handle leading digits
  module_name = re.sub(r'\.\.+', '._', module_name)

  spec = importlib.util.spec_from_file_location(module_name, path)
  module = importlib.util.module_from_spec(spec)
  sys.modules[module_name] = module
  spec.loader.exec_module(module)
  return module


def set_extension(path, ext):
   name, _ = os.path.splitext(path)
   return f'{name}{os.path.extsep}{ext}'

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
