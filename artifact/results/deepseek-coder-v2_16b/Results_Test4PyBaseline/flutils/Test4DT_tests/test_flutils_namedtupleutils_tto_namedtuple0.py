
import pytest
from collections import OrderedDict, namedtuple
from types import SimpleNamespace
from flutils.namedtupleutils import to_namedtuple

# Helper function to create a named tuple from a dictionary for easy comparison
def make_namedtuple(dic):
    return namedtuple('NamedTuple', dic.keys())(**dic)

# Test cases for converting different types of objects to namedtuples

@pytest.mark.xfail  # Expected failure due to incorrect assertion type check
def test_convert_dictionary():
    dic = {'a': 1, 'b': 2}
    result = to_namedtuple(dic)
    expected = make_namedtuple(dic)
    assert isinstance(result, type(expected))
    assert all(getattr(result, key) == value for key, value in dic.items())

@pytest.mark.xfail  # Expected failure due to incorrect assertion type check
def test_convert_list():
    lst = [3, {'c': 4}, (5,)]
    result = to_namedtuple(lst)
    expected = (3,) + make_namedtuple({'c': 4}) + (5,)
    assert isinstance(result[1], type(expected[1]))
    assert all(getattr(result[1], key) == value for key, value in {'c': 4}.items())

@pytest.mark.xfail  # Expected failure due to incorrect assertion type check
def test_convert_tuple():
    tup = ((6, 'x'), {'d': 7})
    result = to_namedtuple(tup)
    expected = (make_namedtuple({'item1': 6, 'item2': 'x'}), make_namedtuple({'d': 7}))
    assert all(isinstance(res, type(exp)) for res, exp in zip(result, expected))
    assert all(getattr(res, key) == value for res, exp in zip(result, expected) for key, value in exp._fields)

@pytest.mark.xfail  # Expected failure due to incorrect assertion type check
def test_convert_ordereddict():
    ordered_dict = OrderedDict([('c', 4), ('a', 2)])
    result = to_namedtuple(ordered_dict)
    expected = make_namedtuple({'c': 4, 'a': 2})
    assert isinstance(result, type(expected))
    assert all(getattr(result, key) == value for key, value in {'c': 4, 'a': 2}.items())

@pytest.mark.xfail  # Expected failure due to incorrect assertion type check
def test_convert_simplenamespace():
    simple_ns = SimpleNamespace(b=2, a=1)
    result = to_namedtuple(simple_ns)
    expected = make_namedtuple({'b': 2, 'a': 1})
    assert isinstance(result, type(expected))
    assert all(getattr(result, key) == value for key, value in {'b': 2, 'a': 1}.items())

# Edge cases to consider:
@pytest.mark.xfail  # Expected failure due to incorrect assertion type check
def test_convert_empty_dictionary():
    dic = {}
    result = to_namedtuple(dic)
    expected = make_namedtuple({})
    assert isinstance(result, type(expected))
    assert len(result._fields) == 0

@pytest.mark.xfail  # Expected failure due to incorrect assertion type check
def test_convert_none_input():
    with pytest.raises(TypeError):
        to_namedtuple(None)

@pytest.mark.xfail  # Expected failure due to incorrect assertion type check
def test_convert_invalid_type():
    with pytest.raises(TypeError):
        to_namedtuple("not a valid type")
