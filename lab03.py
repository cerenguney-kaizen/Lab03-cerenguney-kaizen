# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    # TODO (Part 1): return the Pig Latin form of a single lowercase word.
    #   If it starts with a vowel (a, e, i, o, u): add "way" to the end.
    #   Otherwise: move the first letter to the end and add "ay".
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"
print(pig_latin("ate"))
print(pig_latin("banana"))
print(pig_latin("what"))



def word_lengths(sentence):
    # TODO (Part 2): return a list with the length of each word in `sentence`
    #   (words are separated by spaces).
    lengths = []
    for character in sentence.split():
        lengths.append(len(character))
    return lengths
print(word_lengths("the quick brown fox") )
print(word_lengths("")  )


def reverse_words(sentence):
    # TODO (Part 3): return `sentence` with the order of its words reversed.
    #   e.g. "hello world" -> "world hello"
    words = sentence.split()
    backwards = words[::-1]
    return " ".join(backwards)
print(reverse_words("the quick brown fox"))



def letter_counts(text):
    # TODO (Part 4 - STRETCH, optional): return a dictionary mapping each letter
    #   to how many times it appears in `text`. Ignore case, and ignore anything
    #   that isn't a letter.
    counts = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    return counts
print(letter_counts("hello"))


def main():
    # Optional scratch space - use this to try your functions with sample values.
    # print(pig_latin("banana"))                    # ananabay
    # print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]
    # print(reverse_words("the quick brown fox"))   # fox brown quick the
    # print(letter_counts("hello"))                 # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    pass


if __name__ == "__main__":
    main()
