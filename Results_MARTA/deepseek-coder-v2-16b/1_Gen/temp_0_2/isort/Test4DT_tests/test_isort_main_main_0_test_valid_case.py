
import sys
from io import StringIO
from isort.main import main as isort_main
import pytest

@pytest.mark.parametrize("input_data", [
    "import os\n",  # A valid case with standard input containing an import statement
    "",  # An empty string to test behavior when stdin is empty
])
def test_valid_case(monkeypatch, capsys, input_data):
    monkeypatch.setattr('sys.stdin', StringIO(input_data))
    
    # Mock the X class if necessary for this specific test case
    with pytest.raises(SystemExit) as e:
        isort_main()
    
    assert e.type == SystemExit
    captured = capsys.readouterr()
    assert "Error:" not in captured.out  # Ensure no error messages are printed
