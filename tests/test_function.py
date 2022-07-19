#!/usr/bin/env python

import pkt

@pkt.cloud_function
def f(x):
    return x + 2

print(f(10))
