


def call_or(fn, *arg, default=None):
  try:
    return fn(*arg)
  except:
    return default