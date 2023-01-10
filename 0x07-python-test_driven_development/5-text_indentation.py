#!/usr/bin/python3

def text_indentation(text):

    if type(text) != str:
        raise TypeError("text must be a string")
    toCatAfter=['.', '?', ':']

    idx = 0 
    for items in text:
        if items in toCatAfter:
            if text[idx + 1 ] == " ":
                text = text[:idx + 1] + text[idx + 2:]

        else:
            idx += 1

    print(text, end='')
