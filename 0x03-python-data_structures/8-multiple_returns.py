#!/usr/bin/python3

def multiple_returns(sentence):
    """function returns the length of sentence and its first character"""

    t = sentence
    L = len(t)

    if t != '':
        f = t[0]
        return (L, f)
    else:
        return (L, None)
