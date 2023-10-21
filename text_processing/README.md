# Text Processing Utility Library

The `text_processing` directory offers a suite of functions tailored for common text manipulation, cleaning, tokenization, and pattern matching tasks. This library aims to cover various aspects of text processing, from cleaning up raw data to identifying specific patterns using regular expressions.

## Table of Contents

1. [Cleaning (`cleaner.py`)](#cleaning)
2. [Tokenization (`tokenization.py`)](#tokenization)
3. [Transformation (`transformation.py`)](#transformation)
4. [Analysis (`analysis.py`)](#analysis)
5. [Regular Expressions (`regex.py`)](#regular-expressions)

---

### Cleaning (`cleaner.py`)

Cleaning is the process of preparing your text data by removing or transforming unnecessary, redundant, or noisy elements.

**Functions**:
- **`remove_punctuation(text)`**: Removes all punctuation from the given text.
- **`to_lowercase(text)`**: Converts all characters in the text to lowercase.
- **`simple_csv_parser(text)`**: Parses a simple CSV string into a list of lists.
- **`remove_numeric(text)`**: Strips out all numeric characters from the text.

---

### Tokenization (`tokenization.py`)

Tokenization is the process of splitting text into individual tokens, typically words.

**Functions**:
- **`tokenize_words(text)`**: Splits the text into words.
- **`split_by_whitespace(text)`**: Splits the text by one or more whitespace characters.

---

### Transformation (`transformation.py`)

Transformation involves converting the structure or representation of the text.

**Functions**:
- **`text_to_ascii(text)`**: Converts each character in the text to its ASCII value.

---

### Analysis (`analysis.py`)

Analysis functions help in understanding patterns, computing statistics, or extracting specific information from text.

**Functions**:
- **`word_frequency(text)`**: Computes the frequency of each word in the text.
- **`count_vowels(text)`**: Counts the number of vowels in the text.
- **`most_frequent_word(text)`**: Finds the most frequent word in the text.

---

### Regular Expressions (`regex.py`)

Regular expressions provide a powerful mechanism for matching strings of text, such as particular characters, words, or patterns of characters.

**Functions**:
- **`find_all_emails(text)`**: Extracts all email addresses from the given text.
- **`remove_html_tags(text)`**: Removes all HTML tags from the given text.
- **`extract_numbers(text)`**: Extracts all numbers from the given text.

---

For each function, refer to the respective file for more detailed documentation, usage examples, and further insights. This library serves as a foundational toolkit for various text processing tasks, and can be expanded upon as needed.