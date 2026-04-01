
import pytest
from string_utils.validation import is_snake_case

@pytest.mark.parametrize("input_str, separator, expected", [
    (None, '_', False),
    ('', '_', False),
    ('foo_bar_baz', None, False),  # Invalid separator should be handled by default
    ('foo_bar_baz', '', False),     # Empty string as separator is invalid
    ('foo_bar_baz', ' ', False),    # Space as separator is not allowed
    ('Foo_Bar', '_', False),        # Contains uppercase letters
    ('123_foo', '_', False),        # Starts with a number
    ('foo-bar_baz', '-', True),     # Valid snake case with different separator
])
def test_edge_cases(input_str, separator, expected):
    assert is_snake_case(input_str, separator) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 8 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_edge_cases.py . [ 12%]
.FF.F.F                                                                  [100%]

=================================== FAILURES ===================================
___________________ test_edge_cases[foo_bar_baz-None-False] ____________________

input_str = 'foo_bar_baz', separator = None, expected = False

    @pytest.mark.parametrize("input_str, separator, expected", [
        (None, '_', False),
        ('', '_', False),
        ('foo_bar_baz', None, False),  # Invalid separator should be handled by default
        ('foo_bar_baz', '', False),     # Empty string as separator is invalid
        ('foo_bar_baz', ' ', False),    # Space as separator is not allowed
        ('Foo_Bar', '_', False),        # Contains uppercase letters
        ('123_foo', '_', False),        # Starts with a number
        ('foo-bar_baz', '-', True),     # Valid snake case with different separator
    ])
    def test_edge_cases(input_str, separator, expected):
>       assert is_snake_case(input_str, separator) == expected

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_edge_cases.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/validation.py:337: in is_snake_case
    re.compile(re_template.format(sign=re.escape(separator)), re.IGNORECASE)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

pattern = None

    def escape(pattern):
        """
        Escape special characters in a string.
        """
        if isinstance(pattern, str):
            return pattern.translate(_special_chars_map)
        else:
>           pattern = str(pattern, 'latin1')
E           TypeError: decoding to str: need a bytes-like object, NoneType found

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/re.py:276: TypeError
_____________________ test_edge_cases[foo_bar_baz--False] ______________________

input_str = 'foo_bar_baz', separator = '', expected = False

    @pytest.mark.parametrize("input_str, separator, expected", [
        (None, '_', False),
        ('', '_', False),
        ('foo_bar_baz', None, False),  # Invalid separator should be handled by default
        ('foo_bar_baz', '', False),     # Empty string as separator is invalid
        ('foo_bar_baz', ' ', False),    # Space as separator is not allowed
        ('Foo_Bar', '_', False),        # Contains uppercase letters
        ('123_foo', '_', False),        # Starts with a number
        ('foo-bar_baz', '-', True),     # Valid snake case with different separator
    ])
    def test_edge_cases(input_str, separator, expected):
>       assert is_snake_case(input_str, separator) == expected

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_edge_cases.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/validation.py:337: in is_snake_case
    re.compile(re_template.format(sign=re.escape(separator)), re.IGNORECASE)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/re.py:251: in compile
    return _compile(pattern, flags)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/re.py:303: in _compile
    p = sre_compile.compile(pattern, flags)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/sre_compile.py:788: in compile
    p = sre_parse.parse(p, flags)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/sre_parse.py:955: in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/sre_parse.py:444: in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/sre_parse.py:841: in _parse
    p = _parse_sub(source, state, sub_verbose, nested + 1)
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/sre_parse.py:444: in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = <sre_parse.Tokenizer object at 0x104833af0>
state = <sre_parse.State object at 0x104833b20>, verbose = 0, nested = 3
first = False

    def _parse(source, state, verbose, nested, first=False):
        # parse a simple pattern
        subpattern = SubPattern(state)
    
        # precompute constants into local variables
        subpatternappend = subpattern.append
        sourceget = source.get
        sourcematch = source.match
        _len = len
        _ord = ord
    
        while True:
    
            this = source.next
            if this is None:
                break # end of pattern
            if this in "|)":
                break # end of subpattern
            sourceget()
    
            if verbose:
                # skip whitespace and comments
                if this in WHITESPACE:
                    continue
                if this == "#":
                    while True:
                        this = sourceget()
                        if this is None or this == "\n":
                            break
                    continue
    
            if this[0] == "\\":
                code = _escape(source, this, state)
                subpatternappend(code)
    
            elif this not in SPECIAL_CHARS:
                subpatternappend((LITERAL, _ord(this)))
    
            elif this == "[":
                here = source.tell() - 1
                # character set
                set = []
                setappend = set.append
    ##          if sourcematch(":"):
    ##              pass # handle character classes
                if source.next == '[':
                    import warnings
                    warnings.warn(
                        'Possible nested set at position %d' % source.tell(),
                        FutureWarning, stacklevel=nested + 6
                    )
                negate = sourcematch("^")
                # check remaining characters
                while True:
                    this = sourceget()
                    if this is None:
                        raise source.error("unterminated character set",
                                           source.tell() - here)
                    if this == "]" and set:
                        break
                    elif this[0] == "\\":
                        code1 = _class_escape(source, this)
                    else:
                        if set and this in '-&~|' and source.next == this:
                            import warnings
                            warnings.warn(
                                'Possible set %s at position %d' % (
                                    'difference' if this == '-' else
                                    'intersection' if this == '&' else
                                    'symmetric difference' if this == '~' else
                                    'union',
                                    source.tell() - 1),
                                FutureWarning, stacklevel=nested + 6
                            )
                        code1 = LITERAL, _ord(this)
                    if sourcematch("-"):
                        # potential range
                        that = sourceget()
                        if that is None:
                            raise source.error("unterminated character set",
                                               source.tell() - here)
                        if that == "]":
                            if code1[0] is IN:
                                code1 = code1[1][0]
                            setappend(code1)
                            setappend((LITERAL, _ord("-")))
                            break
                        if that[0] == "\\":
                            code2 = _class_escape(source, that)
                        else:
                            if that == '-':
                                import warnings
                                warnings.warn(
                                    'Possible set difference at position %d' % (
                                        source.tell() - 2),
                                    FutureWarning, stacklevel=nested + 6
                                )
                            code2 = LITERAL, _ord(that)
                        if code1[0] != LITERAL or code2[0] != LITERAL:
                            msg = "bad character range %s-%s" % (this, that)
                            raise source.error(msg, len(this) + 1 + len(that))
                        lo = code1[1]
                        hi = code2[1]
                        if hi < lo:
                            msg = "bad character range %s-%s" % (this, that)
                            raise source.error(msg, len(this) + 1 + len(that))
                        setappend((RANGE, (lo, hi)))
                    else:
                        if code1[0] is IN:
                            code1 = code1[1][0]
                        setappend(code1)
    
                set = _uniq(set)
                # XXX: <fl> should move set optimization to compiler!
                if _len(set) == 1 and set[0][0] is LITERAL:
                    # optimization
                    if negate:
                        subpatternappend((NOT_LITERAL, set[0][1]))
                    else:
                        subpatternappend(set[0])
                else:
                    if negate:
                        set.insert(0, (NEGATE, None))
                    # charmap optimization can't be added here because
                    # global flags still are not known
                    subpatternappend((IN, set))
    
            elif this in REPEAT_CHARS:
                # repeat previous item
                here = source.tell()
                if this == "?":
                    min, max = 0, 1
                elif this == "*":
                    min, max = 0, MAXREPEAT
    
                elif this == "+":
                    min, max = 1, MAXREPEAT
                elif this == "{":
                    if source.next == "}":
                        subpatternappend((LITERAL, _ord(this)))
                        continue
    
                    min, max = 0, MAXREPEAT
                    lo = hi = ""
                    while source.next in DIGITS:
                        lo += sourceget()
                    if sourcematch(","):
                        while source.next in DIGITS:
                            hi += sourceget()
                    else:
                        hi = lo
                    if not sourcematch("}"):
                        subpatternappend((LITERAL, _ord(this)))
                        source.seek(here)
                        continue
    
                    if lo:
                        min = int(lo)
                        if min >= MAXREPEAT:
                            raise OverflowError("the repetition number is too large")
                    if hi:
                        max = int(hi)
                        if max >= MAXREPEAT:
                            raise OverflowError("the repetition number is too large")
                        if max < min:
                            raise source.error("min repeat greater than max repeat",
                                               source.tell() - here)
                else:
                    raise AssertionError("unsupported quantifier %r" % (char,))
                # figure out which item to repeat
                if subpattern:
                    item = subpattern[-1:]
                else:
                    item = None
                if not item or item[0][0] is AT:
>                   raise source.error("nothing to repeat",
                                       source.tell() - here + len(this))
E                   re.error: nothing to repeat at position 19

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/sre_parse.py:669: error
_______________________ test_edge_cases[Foo_Bar-_-False] _______________________

input_str = 'Foo_Bar', separator = '_', expected = False

    @pytest.mark.parametrize("input_str, separator, expected", [
        (None, '_', False),
        ('', '_', False),
        ('foo_bar_baz', None, False),  # Invalid separator should be handled by default
        ('foo_bar_baz', '', False),     # Empty string as separator is invalid
        ('foo_bar_baz', ' ', False),    # Space as separator is not allowed
        ('Foo_Bar', '_', False),        # Contains uppercase letters
        ('123_foo', '_', False),        # Starts with a number
        ('foo-bar_baz', '-', True),     # Valid snake case with different separator
    ])
    def test_edge_cases(input_str, separator, expected):
>       assert is_snake_case(input_str, separator) == expected
E       AssertionError: assert True == False
E        +  where True = is_snake_case('Foo_Bar', '_')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_edge_cases.py:16: AssertionError
_____________________ test_edge_cases[foo-bar_baz---True] ______________________

input_str = 'foo-bar_baz', separator = '-', expected = True

    @pytest.mark.parametrize("input_str, separator, expected", [
        (None, '_', False),
        ('', '_', False),
        ('foo_bar_baz', None, False),  # Invalid separator should be handled by default
        ('foo_bar_baz', '', False),     # Empty string as separator is invalid
        ('foo_bar_baz', ' ', False),    # Space as separator is not allowed
        ('Foo_Bar', '_', False),        # Contains uppercase letters
        ('123_foo', '_', False),        # Starts with a number
        ('foo-bar_baz', '-', True),     # Valid snake case with different separator
    ])
    def test_edge_cases(input_str, separator, expected):
>       assert is_snake_case(input_str, separator) == expected
E       AssertionError: assert False == True
E        +  where False = is_snake_case('foo-bar_baz', '-')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_edge_cases.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_edge_cases.py::test_edge_cases[foo_bar_baz-None-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_edge_cases.py::test_edge_cases[foo_bar_baz--False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_edge_cases.py::test_edge_cases[Foo_Bar-_-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_snake_case_0_test_edge_cases.py::test_edge_cases[foo-bar_baz---True]
========================= 4 failed, 4 passed in 0.08s ==========================
"""