
import pytest
from unittest.mock import patch
from pytutils.memo import lazyproperty

class MyClass:
    @lazyproperty
    def expensive_calculation(self):
        # This computation is expensive and only needed in certain circumstances
        return sum(i**2 for i in range(1000))

def test_lazyproperty():
    obj = MyClass()
    
    # First call should compute the value
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))
    
    # Subsequent calls should use the cached result
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))

@patch('pytutils.memo._pytest.cacheprovider', autospec=True)
def test_lazyproperty_with_mocked_cache(mock_cache):
    # Mock the cache to avoid real cache operations and focus on testing the lazy property itself
    mock_cache.set.side_effect = Exception("Mocking cache creation for tests")
    
    obj = MyClass()
    
    # First call should compute the value
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))
    
    # Subsequent calls should use the cached result
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

../../../dev .F                                                          [100%]

=================================== FAILURES ===================================
_____________________ test_lazyproperty_with_mocked_cache ______________________

args = (), keywargs = {}

    @wraps(func)
    def patched(*args, **keywargs):
>       with self.decoration_helper(patched,
                                    args,
                                    keywargs) as (newargs, newkeywargs):

/usr/local/lib/python3.11/unittest/mock.py:1375: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/contextlib.py:137: in __enter__
    return next(self.gen)
/usr/local/lib/python3.11/unittest/mock.py:1357: in decoration_helper
    arg = exit_stack.enter_context(patching)
/usr/local/lib/python3.11/contextlib.py:517: in enter_context
    result = _enter(cm)
/usr/local/lib/python3.11/unittest/mock.py:1430: in __enter__
    self.target = self.getter()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = 'pytutils.memo._pytest'

    def resolve_name(name):
        """
        Resolve a name to an object.
    
        It is expected that `name` will be a string in one of the following
        formats, where W is shorthand for a valid Python identifier and dot stands
        for a literal period in these pseudo-regexes:
    
        W(.W)*
        W(.W)*:(W(.W)*)?
    
        The first form is intended for backward compatibility only. It assumes that
        some part of the dotted name is a package, and the rest is an object
        somewhere within that package, possibly nested inside other objects.
        Because the place where the package stops and the object hierarchy starts
        can't be inferred by inspection, repeated attempts to import must be done
        with this form.
    
        In the second form, the caller makes the division point clear through the
        provision of a single colon: the dotted name to the left of the colon is a
        package to be imported, and the dotted name to the right is the object
        hierarchy within that package. Only one import is needed in this form. If
        it ends with the colon, then a module object is returned.
    
        The function will return an object (which might be a module), or raise one
        of the following exceptions:
    
        ValueError - if `name` isn't in a recognised format
        ImportError - if an import failed when it shouldn't have
        AttributeError - if a failure occurred when traversing the object hierarchy
                         within the imported package to get to the desired object.
        """
        global _NAME_PATTERN
        if _NAME_PATTERN is None:
            # Lazy import to speedup Python startup time
            import re
            dotted_words = r'(?!\d)(\w+)(\.(?!\d)(\w+))*'
            _NAME_PATTERN = re.compile(f'^(?P<pkg>{dotted_words})'
                                       f'(?P<cln>:(?P<obj>{dotted_words})?)?$',
                                       re.UNICODE)
    
        m = _NAME_PATTERN.match(name)
        if not m:
            raise ValueError(f'invalid format: {name!r}')
        gd = m.groupdict()
        if gd.get('cln'):
            # there is a colon - a one-step import is all that's needed
            mod = importlib.import_module(gd['pkg'])
            parts = gd.get('obj')
            parts = parts.split('.') if parts else []
        else:
            # no colon - have to iterate to find the package boundary
            parts = name.split('.')
            modname = parts.pop(0)
            # first part *must* be a module/package.
            mod = importlib.import_module(modname)
            while parts:
                p = parts[0]
                s = f'{modname}.{p}'
                try:
                    mod = importlib.import_module(s)
                    parts.pop(0)
                    modname = s
                except ImportError:
                    break
        # if we reach this point, mod is the module, already imported, and
        # parts is the list of parts in the object hierarchy to be traversed, or
        # an empty list if just the module is wanted.
        result = mod
        for p in parts:
>           result = getattr(result, p)
E           AttributeError: module 'pytutils.memo' has no attribute '_pytest'

/usr/local/lib/python3.11/pkgutil.py:715: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-3n8itzgn'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-ofxhcw6p'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-kopzjuiz'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_lazyproperty_with_mocked_cache - AttributeError: m...
=================== 1 failed, 1 passed, 3 warnings in 0.15s ====================
"""