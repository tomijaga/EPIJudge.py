from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if L1 == None and L2 == None:
        return None
    elif L1 == None:
        return L2
    elif L2 == None:
        return L1

    SL = None
    if L1.data <= L2.data:
        SL = L1
        L1 = L1.next
    else:
        SL = L2
        L2 = L2.next

    SL.next = merge_two_sorted_lists(L1, L2)
    return SL


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
