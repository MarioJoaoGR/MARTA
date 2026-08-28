
import pytest
from ansible.utils._junit_xml import TestSuite, TestCase
import dataclasses
import datetime
import typing as t

def test_invalid_inputs():
    class InvalidTestSuite(TestSuite):
        cases: t.List[TestCase] = dataclasses.field(default_factory=list)
    
    with pytest.raises(TypeError):
        invalid_suite = InvalidTestSuite()
