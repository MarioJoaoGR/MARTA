
import pytest
from pathlib import Path
from httpie.sessions import Session

def test_invalid_init():
    try:
        session = Session(None)
    except Exception as e:
        assert str(e).startswith("expected str, bytes or os.PathLike object, not NoneType")
