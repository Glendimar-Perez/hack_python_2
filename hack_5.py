"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = ""
    if len(s) <= 2:
        result = s[:2]
    elif len(s) >= 3:
        result = s[:2] + "-"
        if len(s) >= 5:
            result += s[3:5] + "-"
            if len(s) >= 7:
                result += "oo"!= s[1:3] and s[6:8] or s[5:7] + "-"
    return result
