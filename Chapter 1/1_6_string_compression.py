""" 1.6 str compression
aabcccccaaa => a2b1c5a3
upper and lower case alphabet only
if the compressed string not smaller than the original then return the original
"""

def compress(str):
    """
    count the number times every char occurs, store in a dict
    iterate thru char, count in dict.iteritems
    make a string
    compare with original, if not shorter, return the original else the new
    """
    pass
