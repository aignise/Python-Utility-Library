def text_to_ascii(text):
    """
    Convert each character in the text to its ASCII value.

    Args:
    - text (str): Input string.

    Returns:
    - list: List of ASCII values.
    """
    return [ord(char) for char in text]
