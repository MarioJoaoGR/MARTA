
import os
import csv
import codecs
from unittest.mock import patch, mock_open
import pytest
from tornado.locale import load_translations, _translations, _supported_locales, gen_log


def test_edge_case_none():
    with pytest.raises(TypeError):
        load_translations()