
import pytest
from typing import List, Optional
from docstring_parser.common import DocstringParam

class DocstringMeta:
    def __init__(self, args: List[str], description: Optional[str]) -> None:
        self.args = args
        self.description = description

def test_docstring_param_initialization_with_all_details():
    param = DocstringParam(
        args=[],
        description='The x coordinate.',
        arg_name='x',
        type_name='int',
        is_optional=True,
        default='10'
    )
    assert param.args == []
    assert param.description == 'The x coordinate.'
    assert param.arg_name == 'x'
    assert param.type_name == 'int'
    assert param.is_optional is True
    assert param.default == '10'

def test_docstring_param_initialization_without_optional_and_default():
    param = DocstringParam(
        args=['additional_info'],
        description='The y coordinate, must be non-negative.',
        arg_name='y',
        type_name='float',
        is_optional=False,
        default=None
    )
    assert param.args == ['additional_info']
    assert param.description == 'The y coordinate, must be non-negative.'
    assert param.arg_name == 'y'
    assert param.type_name == 'float'
    assert param.is_optional is False
    assert param.default is None

def test_docstring_param_initialization_without_type():
    param = DocstringParam(
        args=[],
        description='A flag indicating whether to enable the feature.',
        arg_name='enable_feature',
        type_name=None,
        is_optional=True,
        default='False'
    )
    assert param.args == []
    assert param.description == 'A flag indicating whether to enable the feature.'
    assert param.arg_name == 'enable_feature'
    assert param.type_name is None
    assert param.is_optional is True
    assert param.default == 'False'

def test_docstring_param_initialization_without_description():
    param = DocstringParam(
        args=['flag'],
        description=None,
        arg_name='verbose',
        type_name='bool',
        is_optional=False,
        default=None
    )
    assert param.args == ['flag']
    assert param.description is None
    assert param.arg_name == 'verbose'
    assert param.type_name == 'bool'
    assert param.is_optional is False
    assert param.default is None

def test_docstring_param_initialization_with_empty_description():
    param = DocstringParam(
        args=[],
        description='',
        arg_name='empty_desc',
        type_name='str',
        is_optional=True,
        default=None
    )
    assert param.args == []
    assert param.description == ''
    assert param.arg_name == 'empty_desc'
    assert param.type_name == 'str'
    assert param.is_optional is True
    assert param.default is None

def test_docstring_param_initialization_with_empty_args():
    param = DocstringParam(
        args=[],
        description='No additional arguments.',
        arg_name='no_args',
        type_name='int',
        is_optional=False,
        default=None
    )
    assert param.args == []
    assert param.description == 'No additional arguments.'
    assert param.arg_name == 'no_args'
    assert param.type_name == 'int'
    assert param.is_optional is False
    assert param.default is None

def test_docstring_param_initialization_with_empty_arg_name():
    param = DocstringParam(
        args=[],
        description='Invalid parameter.',
        arg_name='',
        type_name='str',
        is_optional=True,
        default=None
    )
    assert param.args == []
    assert param.description == 'Invalid parameter.'
    assert param.arg_name == ''
    assert param.type_name == 'str'
    assert param.is_optional is True
    assert param.default is None

def test_docstring_param_initialization_with_none_arg_name():
    param = DocstringParam(
        args=[],
        description='Invalid parameter.',
        arg_name=None,  # type: ignore
        type_name='str',
        is_optional=True,
        default=None
    )
    assert param.args == []
    assert param.description == 'Invalid parameter.'
    assert param.arg_name is None
    assert param.type_name == 'str'
    assert param.is_optional is True
    assert param.default is None
