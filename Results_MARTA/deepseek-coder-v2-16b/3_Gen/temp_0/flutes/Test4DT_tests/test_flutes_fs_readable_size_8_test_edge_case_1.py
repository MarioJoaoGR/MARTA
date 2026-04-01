
from flutes.fs import readable_size

def test_edge_case_1():
    assert readable_size(1024 * 1024) == "1.00M"
    assert readable_size(500000) == "488.28K"
    assert readable_size(123456789) == "117.74M"
