#!/usr/bin/python3

def multiple_returns(sentence):
    _len = len(sentence)
    if _len != 0:
        f_char = sentence[0]
    else:
        f_char = None
    tup = _len, f_char
    return tup
