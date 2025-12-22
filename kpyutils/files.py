import os

def make_parent_dirs(path):
  parent_directory = os.path.dirname(path)

  os.makedirs(parent_directory, exist_ok=True)