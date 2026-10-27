import argparse
from collections import Counter
def count_words(text):
    words = text.lower().split()
    word_counts = Counter(words)
    return word_counts
def main(argv=None):
    parser = argparse.ArgumentParser(description="Count word frequencies in a text file.")
    parser.add_argument("--file", required=True, help="Path to the input text file.")
    parser.add_argument("--top", type=int, default=10, help="Number of top words to display.")
    args = parser.parse_args(argv)
    try:
        with open(args.file, 'r', encoding='utf-8') as file:
            text = file.read()
            word_counts = count_words(text)
            top_n_count = word_counts.most_common(args.top)
            for word, count in top_n_count:
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")

if __name__ == "__main__":
    main()
    