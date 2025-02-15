import os

def create_directory(path):
    """
    Create a new directory at the specified path.
    
    Args:
        path (str): The path of the directory to create.
    
    Raises:
        FileExistsError: If the directory already exists.
        PermissionError: If there are insufficient permissions to create the directory.
        OSError: For other OS-related errors during directory creation.
    
    Returns:
        str: The absolute path of the created directory.
    """
    # Normalize and expand the path
    full_path = os.path.abspath(os.path.expanduser(path))
    
    # Check if directory already exists
    if os.path.exists(full_path):
        raise FileExistsError(f"Directory already exists: {full_path}")
    
    try:
        # Create directory with full nested path support
        os.makedirs(full_path, exist_ok=False)
        return full_path
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot create directory at {full_path}")
    except OSError as e:
        raise OSError(f"Error creating directory: {e}")