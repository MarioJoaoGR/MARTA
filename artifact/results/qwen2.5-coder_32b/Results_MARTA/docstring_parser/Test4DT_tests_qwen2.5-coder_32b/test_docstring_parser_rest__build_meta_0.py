
import pytest
from docstring_parser.rest import _build_meta, DocstringParam


def test_param_without_type():
    meta = _build_meta(['param', 'verbose'], "If True, prints detailed output.")
    assert isinstance(meta, DocstringParam)
    assert meta.arg_name == 'verbose'
    assert meta.type_name is None





