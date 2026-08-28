
import pytest
from unittest.mock import patch
from tornado.util import import_object


def test_import_missing_module():
    with pytest.raises(ImportError) as e:
        import_object('tornado.missing_module')
    assert str(e.value) == "No module named missing_module"


if __name__ == "__main__":
    pytest.main()