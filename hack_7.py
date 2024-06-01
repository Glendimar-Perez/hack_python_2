"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = []
    if not s:
        result.append(0)
    else:
        for index in range(len(s)):
            if s[index] == 0:
                result.append(s[index])
            elif index % 2 == 0:
                result.append(str(index + 1))
            else:
                result.append(index + 1)
    return result
