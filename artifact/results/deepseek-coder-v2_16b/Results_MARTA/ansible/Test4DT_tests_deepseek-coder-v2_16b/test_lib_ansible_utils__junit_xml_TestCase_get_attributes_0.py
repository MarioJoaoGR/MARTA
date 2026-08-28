
import pytest
from ansible.utils._junit_xml import TestCase
import decimal
import typing as t

def test_valid_inputs():
    tc = TestCase(name='test_example', assertions=5, status='passed', time=decimal.Decimal('0.123'))
    attrs = tc.get_attributes()
    assert 'assertions' in attrs
    assert attrs['assertions'] == '5'

def test_missing_assertions():
    tc = TestCase(name='test_example', status='passed', time=decimal.Decimal('0.123'))
    attrs = tc.get_attributes()
    assert 'assertions' not in attrs

def test_empty_testcase():
    tc = TestCase(name='test_example')
    attrs = tc.get_attributes()
    assert 'assertions' not in attrs
    assert 'status' not in attrs
    assert 'time' not in attrs
