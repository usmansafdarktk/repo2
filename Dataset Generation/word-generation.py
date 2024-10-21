import itertools
import csv

start_chars = ['ب', 'ج', 'س', 'ص', 'ط', 'ع', 'ف', 'ق', 'ک', 'ل', 'م', 'ن', 'ہ','ھ', 'ی']
mid_chars = ['ب', 'ج', 'س', 'ص', 'ط', 'ع', 'ف', 'ق', 'ک', 'ل', 'م', 'ن', 'ہ','ھ', 'ی']
end_chars = ['آ','ا', 'ب', 'ج', 'د', 'ر', 'س', 'ص', 'ط', 'ع', 'ف', 'ق', 'ک', 'ل', 'م', 'ن', 'و', 'ہ','ھ', 'ی', 'ے']
urdu_alphabets = [
    'آ','ا', 'ب', 'پ', 'ت', 'ٹ', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ڈ', 'ذ', 'ر', 'ڑ', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ہ','ھ', 'ء', 'ی', 'ے'
]
print(len(urdu_alphabets))
def generate_words():
    words = []

    # Single character words from start_chars
    words.extend(start_chars)

    # # Two character words
    for start in start_chars:
        for end in end_chars:
            words.append(start + end)

    # Three character words
    for start in start_chars:
        for mid in mid_chars:
            for end in end_chars:
                words.append(start + mid + end)

    # Four character words
    for start in start_chars:
        for mid_comb in itertools.product(mid_chars, repeat=2):
            for end in end_chars:
                words.append(start + ''.join(mid_comb) + end)

    # Five character words
    for start in start_chars:
        for mid_comb in itertools.product(mid_chars, repeat=3):
            for end in end_chars:
                words.append(start + ''.join(mid_comb) + end)
    print(len(words))

    return words

def generate_labels(words, alphabet):
    print(len(words),999)
    labels = []
    for word in words:
        # Label is the index of each character in the word + 1
        indexed_name = "_".join(f"{urdu_alphabets.index(char) + 1:02d}" for char in word)
        indexed_name = f"{len(word):02d}_" + indexed_name
        labels.append(indexed_name)
    return labels

# Generate words and labels
words = generate_words()
labels = generate_labels(words, urdu_alphabets)

# Save to CSV file
csv_file = 'Ayesha.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row with Count, Label, Word
    writer.writerow(['Count', '0'])
    writer.writerow(['End', '0'])
    count = 0
    for label, word in zip(labels, words):
        # count += 1
        writer.writerow([label, word])

print(f"Generated {len(words)} words and saved to {csv_file}.")