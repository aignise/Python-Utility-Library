def remove_punctuation(text):
    """
    Remove punctuation from the given text.

    Args:
    - text (str): Input string.

    Returns:
    - str: Text without punctuation.
    """
    import string
    return text.translate(str.maketrans('', '', string.punctuation))

def to_lowercase(text):
    """
    Convert all characters in the text to lowercase.

    Args:
    - text (str): Input string.

    Returns:
    - str: Text in lowercase.
    """
    return text.lower()

def simple_csv_parser(text):
    """
    Parse a simple CSV string into a list of lists.

    Args:
    - text (str): CSV string.

    Returns:
    - list of lists: Parsed data.
    """
    lines = text.strip().split('\n')
    return [line.split(',') for line in lines]

def remove_numeric(text):
    """
    Remove all numeric characters from the given text.

    Args:
    - text (str): Input string.

    Returns:
    - str: Text without numeric characters.
    """
    return ''.join(filter(lambda x: not x.isdigit(), text))