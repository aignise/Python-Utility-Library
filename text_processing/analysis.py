def word_frequency(text):
    """
    Compute the frequency of each word in the text.

    Args:
    - text (str): Input string.

    Returns:
    - dict: Dictionary with words as keys and their frequencies as values.
    """
    words = tokenize_words(text)
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def count_vowels(text):
    """
    Count the number of vowels in the text.

    Args:
    - text (str): Input string.

    Returns:
    - int: Number of vowels.
    """
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in text if char in vowels)
    return count

def most_frequent_word(text):
    """
    Find the most frequent word in the text.

    Args:
    - text (str): Input string.

    Returns:
    - str: Most frequent word.
    """
    frequency = word_frequency(text)
    return max(frequency, key=frequency.get)
