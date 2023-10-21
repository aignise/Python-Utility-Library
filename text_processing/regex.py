import re

def find_all_emails(text):
    """
    Extract all email addresses from the given text.

    Args:
    - text (str): Input string.

    Returns:
    - list: List of email addresses.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def replace_phone_numbers(text, replacement):
    """
    Replace all phone numbers in the given text with a replacement string.

    Args:
    - text (str): Input string.
    - replacement (str): Replacement string.

    Returns:
    - str: Text with phone numbers replaced.
    """
    pattern = r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.sub(pattern, replacement, text)


def extract_urls(text):
    """
    Extract all URLs from the given text.

    Args:
    - text (str): Input string.

    Returns:
    - list: List of URLs.
    """
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(pattern, text)

def remove_html_tags(text):
    """
    Remove all HTML tags from the given text.

    Args:
    - text (str): Input string.

    Returns:
    - str: Text without HTML tags.
    """
    pattern = r'<.*?>'
    return re.sub(pattern, '', text)

def extract_numbers(text):
    """
    Extract all numbers from the given text.

    Args:
    - text (str): Input string.

    Returns:
    - list: List of numbers.
    """
    pattern = r'\d+'
    return re.findall(pattern, text)

# ... More regex functions can be added as needed ...
