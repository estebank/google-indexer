def split(s, sep=None, maxsplit=-1):
    """split(s [,sep [,maxsplit]]) -> list of strings

    Return a list of the words in the string s, using sep as the
    delimiter string.  If maxsplit is given, splits at no more than
    maxsplit places (resulting in at most maxsplit+1 words).  If sep
    is not specified or is None, any whitespace string is a separator.

    (split and splitfields are synonymous)

    """
    return s.split(sep, maxsplit)

split('.')
