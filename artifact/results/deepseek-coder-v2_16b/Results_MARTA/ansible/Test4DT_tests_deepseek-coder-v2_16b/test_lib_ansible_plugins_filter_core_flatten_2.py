
import pytest
from ansible.plugins.filter import core

def is_sequence(element):
    return isinstance(element, list) or isinstance(element, tuple)

def flatten(mylist, levels=None, skip_nulls=True):
    ret = []
    for element in mylist:
        if skip_nulls and element in (None, 'None', 'null'):
            # ignore null items
            continue
        elif is_sequence(element):
            if levels is None:
                ret.extend(flatten(element, skip_nulls=skip_nulls))
            elif levels >= 1:
                # decrement as we go down the stack
                ret.extend(flatten(element, levels=(int(levels) - 1), skip_nulls=skip_nulls))
            else:
                ret.append(element)
        else:
            ret.append(element)
    return ret


def test_flatten_with_specified_levels():
    result = core.flatten([1, [2, [3, [4, 5]]]], levels=2)
    assert result == [1, 2, 3, [4, 5]]

def test_flatten_ignoring_nulls():
    result = core.flatten([1, [2, None, 'null', [3, 4]], [[5, 6], 7]])
    assert result == [1, 2, 3, 4, 5, 6, 7]