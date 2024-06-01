"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = []
    if not s:
        result.append("0")
    else:
        for index in range(len(s)):
            if index % 2 == 0:
                result.append(str(index + 1))
            else:
                result.append("-")
    return result
