"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(data):
    value = {key.capitalize(): "Fooziman" for key, item in data.items() if key.lower() == "foo"}
    return value
