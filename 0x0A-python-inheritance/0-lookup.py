#!/usr/bin/python3
def lookup(obj):
    """ This function  returns the list of available attributes
        and methods of an object

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
