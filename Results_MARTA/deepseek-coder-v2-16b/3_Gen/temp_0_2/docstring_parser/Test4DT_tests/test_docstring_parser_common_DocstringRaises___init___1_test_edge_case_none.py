
import pytest
from docstring_parser.common import T

class DocstringRaises:
    """DocstringMeta symbolizing :raises metadata."""
    def __init__(
        self,
        args: T.List[str],
        description: T.Optional[str],
        type_name: T.Optional[str],
    ) -> None:
        """Initialize self."""
        super().__init__(args, description)
        self.type_name = type_name
        self.description = description

def test_edge_case_none():
    with pytest.raises(TypeError):
        docstring_instance = DocstringRaises(args=None, description=None, type_name=None)
