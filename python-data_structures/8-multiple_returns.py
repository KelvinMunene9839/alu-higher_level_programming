#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return (0, None)
    first = sentence[0] if len(sentence) > 0 else None
    return (len(sentence), first)
