import sys


def msg(str):
  sys.stderr.write(str)
  sys.stderr.write('\n')


def msgProp(prop, val):
  sys.stderr.write(prop)
  sys.stderr.write(": ")
  sys.stderr.write(val)



def in_incl_range(i, strt, end):
  if end < strt:
    nend = strt
    strt = end
    end = nend
  return i >= strt and i <= end


def incl_range(strt, end):
  return range(strt, end + 1)


