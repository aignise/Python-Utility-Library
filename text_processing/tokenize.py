def tokenize_words(text):
    """
    Split text into words.

    Args:
    - text (str): Input string.

    Returns:
    - list: List of words.
    """
    return text.split()

def split_by_whitespace(text):
    """
    Split the text by one or more whitespaces.

    Args:
    - text (str): Input string.

    Returns:
    - list: List of substrings.
    """
    pattern = r'\s+'
    return re.split(pattern, text)
