"""
Copyright 2022, University of Freiburg
Hannah Bast <bast@cs.uni-freiburg.de>
"""

import re
import sys
import numpy


class InvertedIndex:
    """
    A simple inverted index as explained in Lecture 1.
    """

    def __init__(self):
        """
        Creates an empty inverted index.
        """

        self.inverted_lists = {}
        self.terms = []
        self.num_terms = 0
        self.num_docs = 0

    def build_from_file(self, file_name):
        """
        Construct the inverted index from the given file, with one text record
        (document) per line.

        >>> ii = InvertedIndex()
        >>> ii.build_from_file("example.txt")
        >>> sorted(ii.inverted_lists.items())
        [('a', [1, 2]), ('film', [2]), ('movie', [1, 1, 3])]
        >>> ii.terms
        ['a', 'movie', 'film']
        >>> [ii.num_terms, ii.num_docs]
        [3, 3]
        """

        with open(file_name, "r") as file:
            doc_id = 0
            for line in file:
                line = line.strip()
                doc_id += 1

                for term in re.split("[^A-Za-z]+", line):
                    term = term.lower().strip()

                    # Ignore the term if it is empty.
                    if len(term) == 0:
                        continue

                    if term not in self.inverted_lists:
                        self.terms.append(term)
                        self.inverted_lists[term] = []
                    self.inverted_lists[term].append(doc_id)
            self.num_terms = len(self.inverted_lists)
            self.num_docs = doc_id

    def build_term_document_matrix(self):
        """
        Build a term-document matrix from the already constructed inverted
        index.
        """

        A = numpy.zeros((self.num_terms, self.num_docs))
        for term_id, term in enumerate(self.terms):
            for doc_id in self.inverted_lists[term]:
                A[term_id][doc_id - 1] += 1
        return A


if __name__ == "__main__":
    # Parse the command line arguments.
    if len(sys.argv) != 2:
        print("Usage: python3 %s <file>" % sys.argv[0])
        sys.exit()

    file_name = sys.argv[1]

    # Create an inverted index from the given file.
    print("Reading from file '%s'." % file_name)
    ii = InvertedIndex()
    ii.build_from_file(file_name)

    # Build the term-document matrix and show it (and some other stuff).
    A = ii.build_term_document_matrix()
    q = numpy.array([0, 1, 1, 0])
    numpy.set_printoptions(formatter={"float": lambda x: ("%2.0f" % x)})
    print()
    print("Term-document matrix A:")
    print(A)
    print()
    print("Query vector q:")
    print(q)
    print()
    print("Scores:")
    print(q.dot(A))
    print()
