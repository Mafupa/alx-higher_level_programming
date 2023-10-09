#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0:
        tpl = (len(sentence), sentence[0])
        return tpl
    else:
        tpl = (0, None)
        return tpl
