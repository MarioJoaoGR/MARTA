
import pytest
from typing import List, Optional
from docstring_parser.common import DocstringMeta

# Assuming DocstringParam is defined in the same module as DocstringMeta
class DocstringParam(DocstringMeta):
    def __init__(
        self,
        args: List[str],
        description: Optional[str],
        arg_name: str,
        type_name: Optional[str],
        is_optional: Optional[bool],
        default: Optional[str],
    ) -> None:
        super().__init__(args, description)
        self.arg_name = arg_name
        self.type_name = type_name
        self.is_optional = is_optional
        self.default = default


def test_valid_required_param():
    param = DocstringParam(
        args=[],
        description=None,
        arg_name="item_count",
        type_name=None,
        is_optional=False,
        default=None
    )
    assert param.arg_name == "item_count"
    assert param.is_optional is False

def test_valid_optional_param_with_default():
    param = DocstringParam(
        args=["arg1", "arg2"],
        description="The number of items to process.",
        arg_name="item_count",
        type_name="int",
        is_optional=True,
        default="10"
    )
    assert param.arg_name == "item_count"
    assert param.default == "10"

def test_valid_optional_param_without_default():
    param = DocstringParam(
        args=[],
        description="A flag indicating whether to enable the feature.",
        arg_name="enable_feature",
        type_name="bool",
        is_optional=True,
        default=None
    )
    assert param.arg_name == "enable_feature"
    assert param.default is None

def test_valid_required_param_with_type():
    param = DocstringParam(
        args=["required_arg"],
        description="The required input data.",
        arg_name="data",
        type_name="List[str]",
        is_optional=False,
        default=None
    )
    assert param.arg_name == "data"
    assert param.type_name == "List[str]"