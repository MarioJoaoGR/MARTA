
import pytest
from tqdm.contrib.telegram import ttgrange

# Test valid inputs
def test_valid_inputs():
    # Assuming you have obtained your token and chat_id
    with pytest.raises(TypeError):  # ttgrange expects at least one argument for range, but we pass None to trigger an error
        for i in ttgrange(None, token='your_bot_token', chat_id='your_chat_id'):
            pass

# Test edge cases
def test_edge_cases():
    # Test with None as input
    with pytest.raises(TypeError):  # ttgrange expects at least one argument for range, but we pass None to trigger an error
        for i in ttgrange(None, token='your_bot_token', chat_id='your_chat_id'):
            pass

# Test invalid inputs and error handling
def test_invalid_inputs():
    # Test without any arguments
    with pytest.raises(TypeError):  # ttgrange expects at least one argument for range, but we call it without any to trigger an error
        for i in ttgrange():
            pass
