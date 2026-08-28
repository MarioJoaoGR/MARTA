
import re
import pytest
from ansible.module_utils.common.dict_transformations import _camel_to_snake


def test_reversible_false_complex_case():
    result = _camel_to_snake("TargetGroupARNs", False)
    assert result == "target_group_arns"