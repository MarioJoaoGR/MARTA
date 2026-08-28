
# content of test_lib_ansible_cli_doc_DocCLI_init_parser_0.py
import pytest
from ansible.cli.doc import DocCLI


def test_invalid_inputs():
    with pytest.raises(TypeError):
        doc_cli = DocCLI()