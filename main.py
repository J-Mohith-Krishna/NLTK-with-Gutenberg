import nltk
from nltk.corpus import gutenberg
# Download the Gutenberg corpus (if not already downloaded)
nltk.download('gutenberg')

def access_gutenberg_corpus():
    # List available files in the Gutenberg corpus
    print("Available files in Gutenberg Corpus:")
    print(gutenberg.fileids())

    # Access and print the text of a specific document in the corpus
    document_name = '/content/shakespeare-hamlet.txt.txt'
    document_text = gutenberg.raw(document_name)
    print(f"\nText of '{document_name}':\n{document_text[:500]}...")

def main():
    # Access the Gutenberg corpus
    access_gutenberg_corpus()

if __name__ == "__main__":
    main()
