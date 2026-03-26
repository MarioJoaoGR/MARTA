
import pytest

from isort.identify import Import


def test_valid_inputs():
    imp = Import(line_number=10, indented=True, module='mymodule', attribute=None, alias='mc', cimport=False, file_path=None)
    assert str(imp) == ":10 indented import mymodule as mc"
