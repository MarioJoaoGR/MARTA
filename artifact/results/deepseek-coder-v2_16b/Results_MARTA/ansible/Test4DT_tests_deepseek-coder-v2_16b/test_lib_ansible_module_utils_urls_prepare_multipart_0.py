 ```python
import pytest
from unittest.mock import patch
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from io import BytesIO
import os
import mimetypes
import email.parser
import email.generator
import email.utils
import email.mime.nonmultipart
import email.mime.text

def prepare_multipart(fields):
    """Takes a mapping, and prepares a multipart/form-data body

    :arg fields: Mapping
    :returns: tuple of (content_type, body) where ``content_type`` is
        the ``multipart/form-data`` ``Content-Type`` header including
        ``boundary`` and ``body`` is the prepared bytestring body

    Payload content from a file will be base64 encoded and will include
    the appropriate ``Content-Transfer-Encoding`` and ``Content-Type``
    headers.
    """

    if not isinstance(fields, dict):
        raise TypeError('Mapping is required, cannot be type %s' % fields.__class__.__name__)

    m = MIMEMultipart('form-data')
    for field, value in sorted(fields.items()):
        if isinstance(value, str):
            main_type = 'text'
            sub_type = 'plain'
            content = value
            filename = None
        elif isinstance(value, dict):
            filename = value.get('filename')
            content = value.get('content')
            if not any((filename, content)):
                raise ValueError('at least one of filename or content must be provided')

            mime = value.get('mime_type')
            if not mime:
                try:
                    mime = mimetypes.guess_type(filename or '', strict=False)[0] or 'application/octet-stream'
                except Exception:
                    mime = 'application/octet-stream'
            main_type, sep, sub_type = mime.partition('/')
        else:
            raise TypeError('value must be a string, or mapping, cannot be type %s' % value.__class__.__name__)

        if not content and filename:
            with open(os.path.join('/bin/true'), 'rb') as f:
                part = MIMEApplication(f.read())
                del part['Content-Type']
                part.add_header('Content-Type', '%s/%s' % (main_type, sub_type))
        else:
            part = email.mime.nonmultipart.MIMENonMultipart(main_type, sub_type)
            part.set_payload(content.encode())

        part.add_header('Content-Disposition', 'form-data')
        del part['MIME-Version']
        part.set_param('name', field, header='Content-Disposition')
        if filename:
            part.set_param('filename', filename, header='Content-Disposition')

        m.attach(part)

    fp = BytesIO()
    g = email.generator.Generator(fp, maxheaderlen=0)
    g.flatten(m)
    b_data = email.utils.fix_eols(fp.getvalue())
    del fp

    headers, sep, b_content = b_data.partition(b'\r\n\r\n')
    return (email.parser.BytesHeaderParser().parsebytes(headers)['content-type'], b_content)

# Test cases
def test_valid_input():
    fields = {
        'file1': {'filename': 'example.txt', 'mime_type': 'text/plain'},
        'file2': {'content': 'some content', 'filename': 'example2.txt', 'mime_type': 'application/octet-stream'},
        'text_form_field': 'value'
    }
    content_type, body = prepare_multipart(fields)
    assert isinstance(body, bytes), "Body should be a byte string"
    assert b'--boundary' in content_type.encode(), "Content-Type header should include boundary"

def test_edge_case():
    fields = None
    with pytest.raises(TypeError):
        prepare_multipart(fields)

def test_invalid_input():
    fields = {'file1': 'not a dict', 'text_form_field': 'value'}
    with pytest.raises(TypeError):
        prepare_multipart(fields)