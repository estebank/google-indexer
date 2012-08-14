def purge():
    "Clear the regular expression cache"
    _cache.clear()

_cache = {}
_cache_repl = {}

_pattern_type = type(sre_compile.compile("", 0))

_MAXCACHE = 100

def _compile(*key):
    # internal: compile pattern
    cachekey = (type(key[0]),) + key
    p = _cache.get(cachekey)
    if p is not None:
        return p
    pattern, flags = key
    if isinstance(pattern, _pattern_type):
        return pattern
    if not sre_compile.isstring(pattern):
        raise TypeError, "first argument must be string or compiled pattern"
    try:
        p = sre_compile.compile(pattern, flags)
    except error, v:
        raise error, v # invalid expression
    if len(_cache) >= _MAXCACHE:
        _cache.clear()
    _cache[cachekey] = p
    return p
