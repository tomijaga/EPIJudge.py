from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    words = []
    map = {"0": "0", "1": "1", "2": "ABC", "3": "DEF", "4": "GHI", "5": "JKL",
           "6": "MNO", "7": "PQRS", "8": "TUV", "9": "WXYZ"}

    def rec(phone_number: str, word: str):
        if len(phone_number) == 0:
            words.append(word)
            return

        c = phone_number[0]
        chars = map[c]

        phone_number = phone_number[1:]

        for char in chars:
            new_word = word
            new_word += char
            rec(phone_number, new_word)

        # word += char[len(chars) - 1]
        # rec(phone_number, word)

        return

    rec(phone_number, "")

    return words


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
