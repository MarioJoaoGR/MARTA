
import pytest

from isort._vendored.tomli._parser import TOMLDecodeError, load


def test_invalid_file():
    with open("invalid_file.toml", "w") as fp:
        fp.write("this is not a valid toml file")
    
    with pytest.raises(TOMLDecodeError):
        with open("invalid_file.toml", "rb") as fp:
            load(fp)
