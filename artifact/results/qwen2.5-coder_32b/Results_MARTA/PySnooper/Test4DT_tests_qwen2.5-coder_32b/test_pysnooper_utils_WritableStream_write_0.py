
import pytest
from pysnooper.utils import WritableStream

class ConsoleWriter(WritableStream):
    def write(self, s):
        if not isinstance(s, str):
            raise SystemExit("Input must be a string")
        print(s)

def test_valid_string():
    console_writer = ConsoleWriter()
    with pytest.raises(SystemExit) as excinfo:
        console_writer.write(123)
    assert "Input must be a string" in str(excinfo.value)

