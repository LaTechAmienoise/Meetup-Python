#!/usr/bin/env python3

import dis


def hello():
  for i in range(0,100_000_000):
    a=i

dis.dis(hello)
