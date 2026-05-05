import string
from collections import Counter

def analyze_text(text):
    lines = text.split("\n")
    line_count = len(lines)
    char_count = len(text)

    text_clean = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text_clean.split()
    word_count = len(words)

    stop_words = {"is", "the", "a", "for", "this", "and", "to", "in", "of"}
    filtered_words = [w for w in words if w not in stop_words]

    word_freq = Counter(filtered_words)
    most_common = word_freq.most_common(10)

    return line_count, word_count, char_count, most_common