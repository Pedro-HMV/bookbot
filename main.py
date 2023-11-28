def count_words(book: str) -> int:
    words = book.split()
    return len(words)


def count_letters(book: str) -> dict:
    letters = {}
    book = book.lower()
    for char in range(ord("a"), ord("z") + 1):
        letters[chr(char)] = book.count(chr(char))
    return letters


if __name__ == "__main__":
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of Frankenstein ---")
        print(f"{count_words(file_contents)} words found in the document\n\n")
        letter_counts = count_letters(file_contents)
        letters = sorted(list(letter_counts))
        for letter in letters:
            print(
                f"The '{letter[0]}' character was found"
                f" {letter_counts[letter]} times"
            )
