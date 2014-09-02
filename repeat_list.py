#!/usr/bin/env python3
def repeat_list(l, times):
        if times < 0:
                raise ValueError("times argument must be non-negative")
        return l * times

