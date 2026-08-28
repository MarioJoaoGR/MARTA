
import pytest
from youtube_dl.options import parseOpts


def test_edge_cases():
    with pytest.raises(SystemExit) as excinfo:
        parser, opts, args = parseOpts(['https://www.youtube.com/watch?v=dQw4w9WgXcQ', '--json-report', '--json-report-file=pytest_report_deepseek-coder-v2_16b.json'])
    assert excinfo.value.code == 2