#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        length_first_tuple = (len(sentence), sentence[0])
        return length_first_tuple
