"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    vowels = "aeiou"
    symbols = "@3¡0v"
    mapping = dict(zip(vowels, symbols))
    result = "".join(mapping.get(c, c) for c in s)

    if len(s) >= 3:
        return result[0].upper() + result[1:-1] + result[-1].upper()
    else:
        test = ""
        for i, text in enumerate(result):
            if text.isalpha() == True:
                if i == 0 or (i == len(result) - 1 and text.lower() != 'v'):
                    test += text.upper()
                else:
                    test += text
            else:
                test += text
        return test