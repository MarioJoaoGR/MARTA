
import pytest
from pymonet.validation import Validation
from pymonet.box import Box

def test_successful_validation():
    success_validation = Validation(value=42, errors=[])
    assert success_validation.value == 42
    box = success_validation.to_box()
    assert isinstance(box, Box)

def test_transform_to_box_no_errors():
    success_validation = Validation(value=42, errors=[])
    assert success_validation.value == 42
    box = success_validation.to_box()
    assert isinstance(box, Box)

def test_transform_to_box_with_errors():
    failure_validation = Validation(value=None, errors=['Error occurred'])
    assert not failure_validation.is_success()
    box = failure_validation.to_box()
    assert isinstance(box, Box)
