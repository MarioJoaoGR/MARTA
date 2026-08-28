
import pytest
from typesystem.base import Message, Position

def test_valid_input_basic():
    msg = Message(text='This field must not exceed 10 characters.')
    assert msg.text == 'This field must not exceed 10 characters.'
    assert msg.code == "custom"
    assert msg.index == []
    assert msg.start_position is None
    assert msg.end_position is None

def test_error_case_conflicting_params():
    try:
        msg = Message(text='Error with both key and index', key='username', index=['users', 3])
    except AssertionError as e:
        pass

def test_error_case_missing_positional_args():
    try:
        msg = Message(text='Error without position arguments')
    except AssertionError as e:
        pass
