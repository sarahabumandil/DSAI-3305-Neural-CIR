"""
Copyright 2022, University of Freiburg
Chair of Algorithms and Data Structures.
Hannah Bast <bast@cs.uni-freiburg.de>
Claudius Korzen <korzen@cs.uni-freiburg.de>
Patrick Brosi <brosi@cs.uni-freiburg.de>
Natalie Prange <prange@cs.uni-freiburg.de>
"""

import re
import sys
import numpy

from typing import Optional, List, Tuple
from scipy.sparse import csr_matrix
from enum import Enum


class Normalization(Enum):
    L1R = "rl1"
    L1C = "cl1"
    L2R = "rl2"
    L2C = "cl2"


class InvertedIndex:
    """
    An extended version of the inverted index of ES2 that uses Vector Space
    Models.

    For this exercise sheet, you can re-use your implementation from ES 2 or
    build upon the master solution for ES 2. In any case, the code skeleton
    below should be followed and all tests should be implemented.
    """

    def __init__(self):
        """
        Creates an empty inverted index.
        """
        numpy.set_printoptions(formatter={'float': lambda x: ("%.3f" % x)})

        # TODO: add your code

    def build_from_file(self, file_name: str, b: Optional[float] = None,
                        k: Optional[float] = None):
        """
        Construct the inverted index from the given file. The expected format
        of the file is one document per line, in the format
        <title>TAB<description>TAB<num_ratings>TAB<rating>TAB<num_sitelinks>
        Each entry in the inverted list associated to a word should contain a
        document id and a BM25 score. Compute the BM25 scores as follows:

        (1) In a first pass, compute the inverted lists with tf scores (that
            is the number of occurrences of the term within the <title> and the
            <description> of a document). Further, compute the document length
            (DL) for each document (that is the number of terms in the <title>
            and the <description> of a document). Afterwards, compute the
            average document length (AVDL).
        (2) In a second pass, iterate over all inverted lists and replace the
            tf scores by BM25 scores, defined as:
            BM25 = tf * (k+1) / (k * (1 - b + b * DL/AVDL) + tf) * log2(N/df),
            where N is the total number of documents and df is the number of
            documents that contain the term.

        On reading the file, use UTF-8 as the standard encoding. To split the
        texts into terms, use the method introduced in the lecture. Make sure
        that you ignore empty terms.

        >>> ii = InvertedIndex()
        >>> ii.build_from_file("example.tsv", b=0, k=float("inf"))
        >>> inv_lists = sorted(ii.inverted_lists.items())
        >>> [(w, [(i, '%.3f' % tf) for i, tf in l]) for w, l in inv_lists]
        ... # doctest: +NORMALIZE_WHITESPACE
        [('animated', [(1, '0.415'), (2, '0.415'), (4, '0.415')]),
         ('animation', [(3, '2.000')]),
         ('film', [(2, '1.000'), (4, '1.000')]),
         ('movie', [(1, '0.000'), (2, '0.000'), (3, '0.000'), (4, '0.000')]),
         ('non', [(2, '2.000')]),
         ('short', [(3, '1.000'), (4, '2.000')])]

        >>> ii = InvertedIndex()
        >>> ii.build_from_file("example.tsv", b=0.75, k=1.75)
        >>> inv_lists = sorted(ii.inverted_lists.items())
        >>> [(w, [(i, '%.3f' % tf) for i, tf in l]) for w, l in inv_lists]
        ... # doctest: +NORMALIZE_WHITESPACE
        [('animated', [(1, '0.459'), (2, '0.402'), (4, '0.358')]),
         ('animation', [(3, '2.211')]),
         ('film', [(2, '0.969'), (4, '0.863')]),
         ('movie', [(1, '0.000'), (2, '0.000'), (3, '0.000'), (4, '0.000')]),
         ('non', [(2, '1.938')]),
         ('short', [(3, '1.106'), (4, '1.313')])]
        """

        # First pass: Compute (1) the inverted lists with tf scores and (2) the
        # document lengths.
        #
        # TODO: add your code

        # Second pass: Iterate the inverted lists and replace the tf scores by
        # BM25 scores, defined as follows:
        # BM25 = tf * (k + 1) / (k * (1 - b + b * DL / AVDL) + tf) * log2(N/df)
        #
        # TODO: add your code

        pass

    def preprocessing_vsm(self, normalization: Optional[Normalization] = None):
        """
        Compute the sparse term-document matrix from the inverted lists
        computed by the build_from_file() method

        >>> ii = InvertedIndex() # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
        >>> ii.build_from_file("example.tsv", b=0, k=float("inf"))
        >>> ii.preprocessing_vsm()
        >>> print(numpy.round(sorted(ii.td_matrix.todense().tolist()), 3))
        [[0.000 0.000 0.000 0.000]
         [0.000 0.000 1.000 2.000]
         [0.000 0.000 2.000 0.000]
         [0.000 1.000 0.000 1.000]
         [0.000 2.000 0.000 0.000]
         [0.415 0.415 0.000 0.415]]

        Note: for the following test, L1 column normalization is activated!

        >>> ii = InvertedIndex() # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
        >>> ii.build_from_file("example.tsv", b=0.75, k=1.75)
        >>> ii.preprocessing_vsm(normalization=Normalization.L1C)
        >>> print(numpy.round(sorted(ii.td_matrix.todense().tolist()), 3))
        [[0.000 0.000 0.000 0.000]
         [0.000 0.000 0.333 0.518]
         [0.000 0.000 0.667 0.000]
         [0.000 0.293 0.000 0.340]
         [0.000 0.586 0.000 0.000]
         [1.000 0.122 0.000 0.141]]

        Note: for the following test, L2 column normalization is activated!

        >>> ii = InvertedIndex() # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
        >>> ii.build_from_file("example.tsv", b=0.75, k=1.75)
        >>> ii.preprocessing_vsm(normalization=Normalization.L2C)
        >>> print(numpy.round(sorted(ii.td_matrix.todense().tolist()), 3))
        [[0.000 0.000 0.000 0.000]
         [0.000 0.000 0.447 0.815]
         [0.000 0.000 0.894 0.000]
         [0.000 0.440 0.000 0.535]
         [0.000 0.879 0.000 0.000]
         [1.000 0.182 0.000 0.222]]
        """

        # TODO: add your code

        pass

    def l1normalize(self, td_matrix: csr_matrix, rows: bool) -> csr_matrix:
        """
        Normalizes the rows or columns of the given term-document matrix with
        respect to the L1-norm.
        Normalizes the rows if rows is True, otherwise normalizes the columns.

        >>> ii = InvertedIndex() # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
        >>> matrix = csr_matrix([
        ...  [1, 1, 0, 1, 0, 0],
        ...  [1, 0, 1, 1, 0, 0],
        ...  [1, 1, 1, 2, 1, 1],
        ...  [0, 0, 0, 1, 1, 1]
        ... ])
        >>> norm_matrix = ii.l1normalize(matrix, rows=False)
        >>> print(numpy.round(norm_matrix.todense().tolist(), 3))
        [[0.333 0.500 0.000 0.200 0.000 0.000]
         [0.333 0.000 0.500 0.200 0.000 0.000]
         [0.333 0.500 0.500 0.400 0.500 0.500]
         [0.000 0.000 0.000 0.200 0.500 0.500]]
        >>> norm_matrix = ii.l1normalize(matrix, rows=True)
        >>> print(numpy.round(norm_matrix.todense().tolist(), 3))
        [[0.333 0.333 0.000 0.333 0.000 0.000]
         [0.333 0.000 0.333 0.333 0.000 0.000]
         [0.143 0.143 0.143 0.286 0.143 0.143]
         [0.000 0.000 0.000 0.333 0.333 0.333]]
        """

        # TODO: add your code

        pass

    def l2normalize(self, td_matrix: csr_matrix, rows: bool) -> csr_matrix:
        """
        Normalizes the rows or columns of the given term-document matrix with
        respect to the L2-norm.
        Normalizes the rows if rows is True, otherwise normalizes the columns.

        >>> ii = InvertedIndex() # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
        >>> matrix = csr_matrix([
        ...  [1, 1, 0, 1, 0, 0],
        ...  [1, 0, 1, 1, 0, 0],
        ...  [1, 1, 1, 2, 1, 1],
        ...  [0, 0, 0, 1, 1, 1]
        ... ])
        >>> norm_matrix = ii.l2normalize(matrix, rows=False)
        >>> print(numpy.round(norm_matrix.todense().tolist(), 3))
        [[0.577 0.707 0.000 0.378 0.000 0.000]
         [0.577 0.000 0.707 0.378 0.000 0.000]
         [0.577 0.707 0.707 0.756 0.707 0.707]
         [0.000 0.000 0.000 0.378 0.707 0.707]]
        >>> norm_matrix = ii.l2normalize(matrix, rows=True)
        >>> print(numpy.round(norm_matrix.todense().tolist(), 3))
        [[0.577 0.577 0.000 0.577 0.000 0.000]
         [0.577 0.000 0.577 0.577 0.000 0.000]
         [0.333 0.333 0.333 0.667 0.333 0.333]
         [0.000 0.000 0.000 0.577 0.577 0.577]]
        """

        # TODO: add your code

        pass

    def process_query_vsm(self, keywords: List[str]) \
            -> List[Tuple[int, float]]:
        """
        Process the given keyword query as in the process_query_vsm() method of
        ES2, but by using VSM.

        >>> ii = InvertedIndex()
        >>> ii.inverted_lists = {
        ...   "foo": [(1, 0.2), (3, 0.6)],
        ...   "bar": [(1, 0.4), (2, 0.7), (3, 0.5)],
        ...   "baz": [(2, 0.1)]
        ... }
        >>> ii.preprocessing_vsm()
        >>> result = ii.process_query_vsm(["foo", "bar"])
        >>> [(id, "%.1f" % tf) for id, tf in result]
        [(3, '1.1'), (2, '0.7'), (1, '0.6')]

        >>> ii = InvertedIndex()
        >>> ii.inverted_lists = {
        ...   "foo": [(1, 0.2), (3, 0.6)],
        ...   "bar": [(2, 0.4), (3, 0.1), (4, 0.8)]
        ... }
        >>> ii.preprocessing_vsm()
        >>> result = ii.process_query_vsm(["foo", "bar", "foo", "bar"])
        >>> [(id, "%.1f" % tf) for id, tf in result]
        [(4, '1.6'), (3, '1.4'), (2, '0.8'), (1, '0.4')]
        """

        # TODO: add your code

        pass


def main():
    # Parse the command line arguments.
    #
    # TODO: make sure that any normalization you are using above may
    #  be enabled by an additional command line parameter, for example
    #  --l2normalize. Per default, your application should use
    #  no normalization and BM25 scores with b=0.75 and k=1.75 (see
    #  the exercise sheet).
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <file> [<b>] [<k>]")
        sys.exit()

    file_name = sys.argv[1]
    b = float(sys.argv[2]) if len(sys.argv) > 2 else None
    k = float(sys.argv[3]) if len(sys.argv) > 3 else None

    # Create a new inverted index from the given file.
    print(f"Reading from file '{file_name}'.")
    ii = InvertedIndex()
    ii.build_from_file(file_name, b=b, k=k)
    print("Done")
    print("Building sparse term-document matrix.")
    ii.preprocessing_vsm(normalization=Normalization.L2C)
    print("Done")

    while True:
        # Ask the user for a keyword query.
        query = input("\nYour keyword query: ")

        # Split the query into keywords.
        keywords = [x.lower().strip() for x in re.split("[^A-Za-z]+", query)]

        # Process the keywords.
        postings = ii.process_query_vsm(keywords)


if __name__ == "__main__":
    main()
