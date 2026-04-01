
import pytest
from pathlib import Path
from unittest.mock import patch
from isort.identify import Import

def test_error_case_2():
    with pytest.raises(TypeError):
        imp = Import(line_number='notAnInt', module='math', attribute=None, alias=None)
