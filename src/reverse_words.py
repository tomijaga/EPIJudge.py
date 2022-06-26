import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s: List[str]):
    l = len(s)
    reverse(s, 0, l)

    i = 0
    j = 0
    while True:
        try:
            j = s.index(' ', i)
            reverse(s, i, j)
            i = j + 1
        except:
            j = -1
            reverse(s, i, l)
            break

        # print("(i, j)", i, j)


def reverse(s, i, j):
    m = int((j - i)/2)
    for d in range(0, m):
        tmp = s[i + d]
        s[i + d] = s[j - d - 1]
        s[j-d - 1] = tmp
    # print(s, i, j)


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
