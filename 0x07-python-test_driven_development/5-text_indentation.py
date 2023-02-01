#!/usr/bin/python3
"""
This is the module 5-text_indentation
It only has one function called text_indentation
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text(str): the text

    Returns:
        void
    """

    if type(text) != str:
        raise TypeError('text must be a string')

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    text = text.replace('\n ', '\n')
    text = text.replace(' \n', '\n')

    print(text, end='')
