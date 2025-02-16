import pytest
from src.file_extension import get_file_extension

def test_normal_file_extension():
    assert get_file_extension('document.txt') == 'txt'

def test_multiple_dots():
    assert get_file_extension('archive.tar.gz') == 'gz'

def test_uppercase_extension():
    assert get_file_extension('image.JPG') == 'jpg'

def test_no_extension():
    assert get_file_extension('no_extension') == ''

def test_hidden_file():
    assert get_file_extension('.bashrc') == ''

def test_file_with_leading_dot():
    assert get_file_extension('.file.txt') == 'txt'

def test_path_with_directory():
    assert get_file_extension('/home/user/document.docx') == 'docx'

def test_empty_string():
    assert get_file_extension('') == ''

def test_dot_at_end():
    assert get_file_extension('filename.') == ''