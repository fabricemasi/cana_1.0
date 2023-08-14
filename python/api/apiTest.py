# coding: utf-8
# !/usr/bin/python

import inspect


def tt(*args):
    caller_frame = inspect.currentframe().f_back
    caller_locals = caller_frame.f_locals
    for arg in args:
        var_name = [name for name, value in caller_locals.items() if value is arg][0]
        print(f"{var_name} = {arg}")
