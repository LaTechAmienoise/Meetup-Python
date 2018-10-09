#!/usr/bin/env python3

from numba import jit

@jit(nopython=True)
def hello():
  for i in range(0,100_000_000):
    a=i

hello()

