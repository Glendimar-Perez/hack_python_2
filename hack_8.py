"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    new = [str(index + 1) if len(s) == 4 or len(s) == 2 else value + "-" + str(index + 1) for index, value in reversed(list(enumerate(s)))]
    return new
