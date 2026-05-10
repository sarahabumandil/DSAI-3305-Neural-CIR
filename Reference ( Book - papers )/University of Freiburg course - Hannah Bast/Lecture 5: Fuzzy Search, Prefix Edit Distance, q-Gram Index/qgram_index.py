"""
Copyright 2019, University of Freiburg
Chair of Algorithms and Data Structures.
Hannah Bast <bast@cs.uni-freiburg.de>
Claudius Korzen <korzen@cs.uni-freiburg.de>
Patrick Brosi <brosi@cs.uni-freiburg.de>
"""

import readline  # NOQA
import sys

from typing import List, Tuple

# Uncomment to use C version of prefix edit distance calculation.
# You have to install the module using the provided ped_c/setup.py
# first.
# from ped_c import ped

# Comment to use C version of prefix edit distance calculation
from ped_python import ped


class QGramIndex:
    """
    A QGram-Index.
    """

    def __init__(self, q: int):
        """
        Creates an empty qgram index.
        """

        self.q = q
        self.inverted_lists = {}  # The inverted lists
        self.padding = "$" * (q - 1)

        # TODO: add your code
        pass

    def build_from_file(self, file_name: str):
        """
        Builds the index from the given file (one line per entity, see ES5).

        The entity IDs are one-based (starting with one).

        The test expects the index to store tuples (<entity id>, <frequency>),
        for each q-gram, where <entity id> is the ID of the entity the
        q-gram appears in, and <frequency> is the number of times it appears
        in the entity.

        For example, the 3-gram "rei" appears 1 time in entity 1 ("frei") and
        one time in entity 2 ("brei"), so its inverted list is
        [(1, 1), (2, 1)].

        >>> qi = QGramIndex(3)
        >>> qi.build_from_file("test.tsv")
        >>> sorted(qi.inverted_lists.items())
        ... # doctest: +NORMALIZE_WHITESPACE
        [('$$b', [(2, 1)]), ('$$f', [(1, 1)]), ('$br', [(2, 1)]),
         ('$fr', [(1, 1)]), ('bre', [(2, 1)]), ('fre', [(1, 1)]),
         ('rei', [(1, 1), (2, 1)])]
        """

        # Code from lecture 5
        with open(file_name, "r") as file:
            entity_id = 0
            for line in file:
                entity_name, rest_of_line = line.strip().split("\t", 1)
                entity_name = entity_name.lower()
                entity_id += 1

                for qgram in self.compute_qgrams(entity_name):
                    if qgram not in self.inverted_lists:
                        # If qgram is seen for the first time, create new list.
                        self.inverted_lists[qgram] = []
                    self.inverted_lists[qgram].append(entity_id)

        # TODO: add your code

    def normalize(self, word: str) -> str:
        """
        Normalize the given string (remove non-word characters and lower case).

        >>> qi = QGramIndex(3)
        >>> qi.normalize("freiburg")
        'freiburg'
        >>> qi.normalize("Frei, burG !?!")
        'freiburg'
        """

        low = word.lower()
        return ''.join([i for i in low if i.isalnum()])

    def compute_qgrams(self, word: str) -> List[str]:
        """
        Compute q-grams for padded version of given string.

        >>> qi = QGramIndex(3)
        >>> qi.compute_qgrams("freiburg")
        ['$$f', '$fr', 'fre', 'rei', 'eib', 'ibu', 'bur', 'urg']
        """

        # TODO: add your code
        pass

    def merge_lists(self, lists: List[List[Tuple[int, int]]])\
            -> List[Tuple[int, int]]:
        """
        Merges the given inverted lists. The tests assume that the
        inverted lists keep count of the entity ID in the list,
        for example, in the first test below, entity 3 appears
        1 time in the first list, and 2 times in the second list.
        After the merge, it occurs 3 times in the merged list.

        >>> qi = QGramIndex(3)
        >>> qi.merge_lists([[(1, 2), (3, 1), (5, 1)],
        ...                 [(2, 1), (3, 2), (9, 2)]])
        [(1, 2), (2, 1), (3, 3), (5, 1), (9, 2)]
        >>> qi.merge_lists([[(1, 2), (3, 1), (5, 1)], []])
        [(1, 2), (3, 1), (5, 1)]
        >>> qi.merge_lists([[], []])
        []
        """

        # TODO: add your code
        pass

    def find_matches(self, prefix: str, delta: int)\
            -> Tuple[List[Tuple[int, int, int]], int]:
        """
        Finds all entities y with PED(x, y) <= delta for a given integer delta
        and a given (normalized) prefix x.

        The test checks for a tuple that contains (1) a list of triples
        containing the entity ID, the PED distance and its score and (2) the
        number of PED calculations

        ([(entity id, PED, score), ...], #ped calculations)

        The entity IDs are one-based (starting with 1).

        >>> qi = QGramIndex(3)
        >>> qi.build_from_file("test.tsv")
        >>> qi.find_matches("frei", 0)
        ([(1, 0, 3)], 1)
        >>> qi.find_matches("frei", 2)
        ([(1, 0, 3), (2, 1, 2)], 2)
        >>> qi.find_matches("freibu", 2)
        ([(1, 2, 3)], 2)
        """

        # TODO: add your code
        pass

    def rank_matches(self, matches: List[Tuple[int, int, int]])\
            -> List[Tuple[int, int, int]]:
        """
        Ranks the given list of (entity id, PED, s), where PED is the PED
        value and s is the popularity score of an entity.

        The test check for a list of triples containing the entity ID,
        the PED distance and its score:

        [(entity id, PED, score), ...]

        >>> qi = QGramIndex(3)
        >>> qi.rank_matches([(1, 0, 3), (2, 1, 2), (2, 1, 3), (1, 0, 2)])
        [(1, 0, 3), (1, 0, 2), (2, 1, 3), (2, 1, 2)]
        """

        # TODO: add your code
        pass


def main():
    """
    Builds a qgram index from the given file and then, in an infinite loop,
    lets the user type a query and shows the result for the normalized query.
    """
    # Parse the command line arguments.
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <file>")
        sys.exit()

    file_name = sys.argv[1]

    # TODO: add your code
    pass


if __name__ == "__main__":
    main()
