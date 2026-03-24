import string

paragraph = """
    This is a multi line string. It can be used to write a long string that spans multiple lines. 
    It can also be used to write more stuff. 
    The purpose of this string is to be used for day 2 exercise 1 for the 2026 python training. 
    It is hoped that this training will end soon.
"""

def word_frequency(text):
    # Lowercase the text
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words
    words = text.split()
    
    # Count frequencies
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq


# Get word frequencies
frequencies = word_frequency(paragraph)

# Sort and get top 5 most common words
top_5 = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:5]

# Print results
print("Top 5 most common words:")
for word, count in top_5:
    print(f"{word}: {count}")