import os
import pytest
import tempfile
from src.directory_creator import create_directory

def test_create_directory_success():
    """Test creating a new directory successfully."""
    with tempfile.TemporaryDirectory() as temp_dir:
        new_dir_path = os.path.join(temp_dir, 'new_test_directory')
        result = create_directory(new_dir_path)
        assert result == os.path.abspath(new_dir_path)
        assert os.path.exists(new_dir_path)
        assert os.path.isdir(new_dir_path)

def test_create_directory_nested():
    """Test creating a nested directory structure."""
    with tempfile.TemporaryDirectory() as temp_dir:
        nested_dir_path = os.path.join(temp_dir, 'parent', 'child', 'grandchild')
        result = create_directory(nested_dir_path)
        assert result == os.path.abspath(nested_dir_path)
        assert os.path.exists(nested_dir_path)
        assert os.path.isdir(nested_dir_path)

def test_create_existing_directory():
    """Test that creating an existing directory raises FileExistsError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        existing_dir = os.path.join(temp_dir, 'existing_dir')
        os.makedirs(existing_dir)
        
        with pytest.raises(FileExistsError) as excinfo:
            create_directory(existing_dir)
        
        assert str(excinfo.value) == f"Directory already exists: {os.path.abspath(existing_dir)}"

def test_create_directory_invalid_path(monkeypatch):
    """Test creating a directory with an invalid path."""
    def mock_makedirs(path, exist_ok=False):
        raise OSError("Mocked OS error")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        invalid_path = os.path.join(temp_dir, '/invalid/path/with/no/permissions')
        monkeypatch.setattr(os, 'makedirs', mock_makedirs)
        
        with pytest.raises(OSError):
            create_directory(invalid_path)