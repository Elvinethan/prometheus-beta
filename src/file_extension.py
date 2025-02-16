def get_file_extension(file_path):
    """
    Get the file extension of a given file path.
    
    Args:
        file_path (str): The path to the file.
    
    Returns:
        str: The file extension in lowercase, without the dot. 
             Returns an empty string if no extension is found.
    
    Examples:
        >>> get_file_extension('document.txt')
        'txt'
        >>> get_file_extension('image.JPG')
        'jpg'
        >>> get_file_extension('no_extension')
        ''
    """
    # Split the filename
    parts = file_path.split('/')
    # Get the last part (filename)
    filename = parts[-1]
    
    # Split the filename by dots
    dot_parts = filename.split('.')
    
    # If filename starts with a dot, or has no dots, or only the last dot is at the end
    if filename.startswith('.') and len(dot_parts) <= 2:
        return ''
    
    # If only one part (no dots) or ends with a dot
    if len(dot_parts) == 1 or dot_parts[-1] == '':
        return ''
    
    # Return the last part (extension) in lowercase
    return dot_parts[-1].lower()