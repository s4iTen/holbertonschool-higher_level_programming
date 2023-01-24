#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0 or sentence[0] is None:
        return (0, None)
    return (len(sentence), sentence[0][0])
