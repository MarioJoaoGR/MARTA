
import pytest
from dataclasses_json import config, Undefined
from marshmallow import fields
from typing import Callable, Dict, Optional, Union

# Test scenario 1: Registering an encoder and decoder for int type

# Test scenario 2: Handling undefined parameters with Undefined.EXCLUDE
def test_config_with_undefined():
    metadata = {}
    new_metadata = config(metadata, undefined=Undefined.EXCLUDE)
    assert 'undefined' in new_metadata['dataclasses_json']
    assert new_metadata['dataclasses_json']['undefined'] == Undefined.EXCLUDE

# Test scenario 3: Custom field name and exclusion function
def test_config_with_field_name_and_exclude():
    def camel_case(field_name):
        return ''.join([word.capitalize() for word in field_name.split('_')])
    
    metadata = {}
    exclude_func = lambda f, t: f == 'email'
    new_metadata = config(metadata, letter_case=camel_case, exclude=exclude_func)
    
    assert 'letter_case' in new_metadata['dataclasses_json']
    assert 'exclude' in new_metadata['dataclasses_json']
    assert new_metadata['dataclasses_json']['letter_case'] == camel_case
    assert callable(new_metadata['dataclasses_json']['exclude'])
    assert new_metadata['dataclasses_json']['exclude']('email', None) is True

if __name__ == "__main__":
    pytest.main()