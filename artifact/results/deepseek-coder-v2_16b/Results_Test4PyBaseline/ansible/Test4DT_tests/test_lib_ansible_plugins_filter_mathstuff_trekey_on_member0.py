# Module: ansible.plugins.filter.mathstuff
import pytest
from ansible.plugins.filter import mathstuff
from collections.abc import Mapping, Iterable
from jinja2.exceptions import UndefinedError
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError

# Test cases for rekey_on_member function
def test_rekey_on_member_dict_of_dicts():
    data = {'1': {'id': 1, 'name': 'Alice'}, '2': {'id': 2, 'name': 'Bob'}}
    new_dict = mathstuff.rekey_on_member(data, 'id')
    assert new_dict == {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}

def test_rekey_on_member_list_of_dicts():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    new_dict = mathstuff.rekey_on_member(data, 'name')
    assert new_dict == {'Alice': {'id': 1, 'name': 'Alice'}, 'Bob': {'id': 2, 'name': 'Bob'}}

def test_rekey_on_member_duplicates_error():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 1, 'name': 'Bob'}]
    with pytest.raises(AnsibleFilterError) as e:
        mathstuff.rekey_on_member(data, 'id', 'error')
    assert str(e.value) == "Key 1 is not unique, cannot correctly turn into dict"

def test_rekey_on_member_duplicates_overwrite():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    new_dict = mathstuff.rekey_on_member(data, 'id', 'overwrite')
    assert new_dict == {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}

def test_rekey_on_member_invalid_duplicates():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    with pytest.raises(AnsibleFilterError) as e:
        mathstuff.rekey_on_member(data, 'id', 'invalid')
    assert str(e.value) == "duplicates parameter to rekey_on_member has unknown value: invalid"

def test_rekey_on_member_non_dict_input():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    with pytest.raises(AnsibleFilterTypeError) as e:
        mathstuff.rekey_on_member(data, 'id')
    assert str(e.value).startswith("Type is not a valid list, set, or dict")

def test_rekey_on_member_non_dict_items():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob', 'extra': 'value'}]
    with pytest.raises(AnsibleFilterTypeError) as e:
        mathstuff.rekey_on_member(data, 'id')
    assert str(e.value).startswith("List item is not a valid dict")

def test_rekey_on_member_missing_key():
    data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    with pytest.raises(AnsibleFilterError) as e:
        mathstuff.rekey_on_member(data, 'non_existent')
    assert str(e.value) == "Key non_existent was not found"
