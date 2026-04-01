
import pytest
from docstring_parser.common import T

class DocstringMeta:
    """Docstring meta information.
    
    Symbolizes lines in form of
    
        :param arg: description
        :raises ValueError: if something happens
    """
    def __init__(
        self, args: T.List[str], description: T.Optional[str]
    ) -> None:
        """Initialize self.

        :param args: list of arguments. The exact content of this variable is
            dependent on the kind of docstring; it's used to distinguish
            between custom docstring meta information items.
        :param description: associated docstring description.
        """
        if not isinstance(args, list):
            raise ValueError("args must be a list")
        self.args = args
        self.description = description

def test_invalid_inputs():
    with pytest.raises(ValueError):
        DocstringMeta(args="not_a_list", description=None)
