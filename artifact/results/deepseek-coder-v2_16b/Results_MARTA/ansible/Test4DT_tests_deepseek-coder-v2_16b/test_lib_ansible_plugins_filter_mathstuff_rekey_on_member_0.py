
import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from collections.abc import Mapping, Iterable

# Assuming the function is defined in a module named 'ansible.plugins.filter.mathstuff'
def rekey_on_member(data, key, duplicates='error'):
    if duplicates not in ('error', 'overwrite'):
        raise AnsibleFilterError("duplicates parameter to rekey_on_member has unknown value: {0}".format(duplicates))

    new_obj = {}

    bool(data) and bool(key)

    if isinstance(data, Mapping):
        iterate_over = data.values()
    elif isinstance(data, Iterable) and not isinstance(data, (str, bytes)):
        iterate_over = data
    else:
        raise AnsibleFilterTypeError("Type is not a valid list, set, or dict")

    for item in iterate_over:
        if not isinstance(item, Mapping):
            raise AnsibleFilterTypeError("List item is not a valid dict")

        try:
            key_elem = item[key]
        except KeyError:
            raise AnsibleFilterError("Key {0} was not found".format(key))
        except TypeError as e:
            raise AnsibleFilterTypeError(str(e))
        except Exception as e:
            raise AnsibleFilterError(str(e))

        if new_obj.get(key_elem, None):
            if duplicates == 'error':
                raise AnsibleFilterError("Key {0} is not unique, cannot correctly turn into dict".format(key_elem))
            elif duplicates == 'overwrite':
                new_obj[key_elem] = item
        else:
            new_obj[key_elem] = item

    return new_obj

# Test cases for each scenario
def test_valid_case_1():
    data = {'a': {'id': 1, 'name': 'Alice'}, 'b': {'id': 2, 'name': 'Bob'}}
    key = 'id'
    result = rekey_on_member(data, key)
    assert result == {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}

def test_valid_case_2():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    key = 'id'
    result = rekey_on_member(data, key)
    assert result == {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}

def test_error_case_1():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 1, 'name': 'Bob'}]
    key = 'id'
    duplicates = 'error'
    with pytest.raises(AnsibleFilterError) as excinfo:
        rekey_on_member(data, key, duplicates)
    assert "Key 1 is not unique" in str(excinfo.value)

def test_error_case_2():
    data = 'not a valid data structure'
    key = 'id'
    with pytest.raises(AnsibleFilterTypeError):
        rekey_on_member(data, key)

def test_error_case_3():
    data = {'a': {'id': 1, 'name': 'Alice'}, 'b': {'id': 2, 'name': 'Bob'}}
    key = 'non_existent'
    with pytest.raises(AnsibleFilterError) as excinfo:
        rekey_on_member(data, key)
    assert "Key non_existent was not found" in str(excinfo.value)

def test_error_case_4():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    key = 'id'
    duplicates = 'invalid'
    with pytest.raises(AnsibleFilterError) as excinfo:
        rekey_on_member(data, key, duplicates)
    assert "duplicates parameter to rekey_on_member has unknown value" in str(excinfo.value)
