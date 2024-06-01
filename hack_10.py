"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""
def fn_hack_10(data):
    list = []
    i = 1
    for item in data:
        item = {str(i): str(i + 1) for value in item.values()}
        i += 2
        list.append(item)
    return list

