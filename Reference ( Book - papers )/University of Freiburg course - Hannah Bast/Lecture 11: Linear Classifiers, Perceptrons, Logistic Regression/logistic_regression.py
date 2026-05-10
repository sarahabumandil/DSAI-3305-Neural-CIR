"""
Copyright 2023, University of Freiburg
Chair of Algorithms and Data Structures

Elmar Haussmann <haussmann@cs.uni-freiburg.de>
Claudius Korzen <korzen@cs.uni-freiburg.de>
Patrick Brosi <brosi@cs.uni-freiburg.de>
Natalie Prange <prange@cs.uni-freiburg.de>
"""
from typing import Tuple, Dict, Optional

import numpy
from scipy.sparse import csr_matrix, hstack
import sys
import re

numpy.set_printoptions(formatter={'float': lambda x: ("%.3f" % x)})


def generate_vocabularies(filename: str) -> Tuple[Dict[str, int],
                                                  Dict[str, int]]:
    """
    Reads the given file and generates vocabularies mapping from label/class to
    label ids and from word to word id.

    You should call this ONLY on your training data.
    """

    # Map from label/class to label id.
    class_vocabulary = dict()

    # Map from word to word id.
    word_vocabulary = dict()

    class_id = 0
    word_id = 0

    # Read the file (containing the training data).
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            label, text = line.strip().split('\t')

            if label not in class_vocabulary:
                class_vocabulary[label] = class_id
                class_id += 1

            # Remove all non-characters and non-digits from the text.
            text = re.sub("\\W+", " ", text.lower())
            # Split the text into words.
            words = text.split()

            # Add the words to the vocabulary.
            for word in words:
                if word not in word_vocabulary:
                    word_vocabulary[word] = word_id
                    word_id += 1

    return word_vocabulary, class_vocabulary


def read_labeled_data(filename: str, class_vocab: Dict[str, int],
                      word_vocab: Dict[str, int]) \
        -> Tuple[csr_matrix, numpy.array]:
    """
    Reads the given file and returns a sparse document-term matrix as well as a
    list of labels of each document. You need to provide a class and word
    vocabulary. Words not in the vocabulary are ignored. Documents labeled
    with classes not in the class vocabulary are also ignored.

    The returned document-term matrix X has size n x m, where n is the number
    of documents and m the number of word ids. The value at i, j denotes the
    number of times word id j is present in document i.

    The returned labels vector y has size n (one label for each document). The
    value at index j denotes the label (class id) of document j.

    >>> wv, cv = generate_vocabularies("example_train.txt")
    >>> X, y = read_labeled_data("example_train.txt", cv, wv)
    >>> X.todense()  # the term document matrix
    matrix([[2.000, 1.000],
            [5.000, 2.000],
            [3.000, 5.000],
            [3.000, 2.000],
            [1.000, 3.000],
            [2.000, 4.000],
            [1.000, 3.000]])
    >>> y  # the array of labels
    array([0, 0, 1, 0, 1, 1, 1])
    """

    labels = []
    row, col, value = [], [], []
    num_examples = 0
    num_cols = len(word_vocab)

    with open(filename, "r") as f:
        for i, line in enumerate(f):
            label, text = line.strip().split('\t')

            if label in class_vocab:
                num_examples += 1
                labels.append(class_vocab[label])
                words = re.sub("\\W+", " ", text.lower()).split()
                for w in words:
                    if w in word_vocab:
                        w_id = word_vocab[w]
                        row.append(i)
                        col.append(w_id)
                        # Duplicate values at the same position i,j are summed.
                        value.append(1.0)

    x = csr_matrix((value, (row, col)), shape=(num_examples, num_cols))
    y = numpy.array(labels)
    return x, y


class LogisticRegression(object):

    def __init__(self, num_classes: int, num_features: int):
        # Remember to account for the bias vector
        self.num_features = num_features + 1
        self.num_classes = num_classes

        # ws stores the normal vector of the separating hyperplane for each
        # class. We begin with w = (0, ...., 0) for each class.
        self.ws = numpy.zeros((self.num_classes, self.num_features))

    def add_bias(self, X: csr_matrix) -> csr_matrix:
        """
        Adds the bias term to the given matrix. You can use this method in your train
        and predict method.

        >>> wv, cv = generate_vocabularies("example_train.txt")
        >>> X, y = read_labeled_data("example_train.txt", cv, wv)
        >>> lr = LogisticRegression(len(cv), len(wv))
        >>> lr.add_bias(X).todense()
        matrix([[1.000, 2.000, 1.000],
                [1.000, 5.000, 2.000],
                [1.000, 3.000, 5.000],
                [1.000, 3.000, 2.000],
                [1.000, 1.000, 3.000],
                [1.000, 2.000, 4.000],
                [1.000, 1.000, 3.000]])
        """
        return csr_matrix(hstack((numpy.ones((X.shape[0], 1)), X)))

    def train(self, X: csr_matrix, y: numpy.array, epochs: Optional[int] = 20,
              alpha: Optional[float] = 0.25, batch_size: Optional[int] = 10,
              verbose: Optional[bool] = False):
        """
        Trains on the sparse document-term matrix X and associated labels y.

        We calculate a weight vector w_c for each class, stored in the
        m * n matrix self.ws, where m is the number of classes, and n is the
        number of features.
        This means we can retrieve the weight vector for a single class c via
        self.ws[c, :]

        Training should be done in batches of size batch_size, as explained
        in the lecture.

        A single epoch updates the weight vectors for each class with each
        batch.

        For the tests, we assume that the normal vector for each class is the
        zero vector in the beginning (like described in the lecture).

        >>> wv, cv = generate_vocabularies("example_train.txt")
        >>> X, y = read_labeled_data("example_train.txt", cv, wv)
        >>> lr = LogisticRegression(len(cv), len(wv))
        >>> lr.train(X, y, epochs=1, alpha=1, batch_size=1)
        >>> numpy.round(lr.ws, 3)
        array([[0.498, 1.008, -2.503],
               [-0.498, -1.008, 2.503]])
        >>> lr = LogisticRegression(len(cv), len(wv))
        >>> lr.train(X, y, epochs=1, alpha=1, batch_size=10)
        >>> numpy.round(lr.ws, 3)
        array([[-0.071, 0.214, -0.714],
               [0.071, -0.214, 0.714]])
        >>> lr = LogisticRegression(len(cv), len(wv))
        >>> lr.train(X, y, epochs=10, alpha=0.1, batch_size=10)
        >>> numpy.round(lr.ws, 3)
        array([[0.001, 0.321, -0.419],
               [-0.001, -0.321, 0.419]])
        """

        # TODO: add your code
        pass

    def predict(self, X: csr_matrix) -> numpy.array:
        """
        Predicts a label for each example in the document-term matrix,
        based on the learned probabilities stored in this class.

        Returns a list of predicted label ids.

        >>> wv, cv = generate_vocabularies("example_train.txt")
        >>> X, y = read_labeled_data("example_train.txt", cv, wv)
        >>> lr = LogisticRegression(len(cv), len(wv))
        >>> lr.train(X, y, epochs=10, alpha=0.1, batch_size=10)
        >>> X_test, y_test = read_labeled_data("example_test.txt", cv, wv)
        >>> lr.predict(X_test)
        array([0, 1, 0])
        >>> lr.predict(X)
        array([0, 0, 1, 0, 1, 1, 1])
        """

        # TODO: add your code
        pass

    def evaluate(self, x: csr_matrix, y: numpy.array) \
            -> Tuple[Dict[int, float], Dict[int, float], Dict[int, float]]:
        """
        Predict the labels of X and return three
        dictionaries mapping from class id to corresponding
        precision/recall/f-measure.

        >>> wv, cv = generate_vocabularies("example_train.txt")
        >>> X_train, y_train = read_labeled_data("example_train.txt", cv, wv)
        >>> X_test, y_test = read_labeled_data("example_test.txt", cv, wv)
        >>> lr = LogisticRegression(len(cv), len(wv))
        >>> lr.train(X_train, y_train)
        >>> precisions, recalls, f1_scores = lr.evaluate(X_test, y_test)
        >>> precisions
        {0: 0.5, 1: 1.0}
        >>> recalls
        {0: 1.0, 1: 0.5}
        >>> {x: '%.2f' % f1_scores[x] for x in f1_scores}
        {0: '0.67', 1: '0.67'}
        """

        # Predict the classes for the test data.
        predictions = self.predict(x)

        # Count the number of times, class i was predicted.
        n_pred_total = {i: 0 for i in range(self.num_classes)}

        # Count the number of docs that have class i in the test data.
        n_total = {i: 0 for i in range(self.num_classes)}

        # Count the number of correct predictions.
        n_correct = {i: 0 for i in range(self.num_classes)}

        for pred, corr in zip(predictions, y):
            n_total[corr] += 1
            n_pred_total[pred] += 1
            if pred == corr:
                n_correct[corr] += 1

        # Compute the precisions, recalls and f-measures per class.
        recalls, precisions, fms = {}, {}, {}
        for i in range(self.num_classes):
            recalls[i] = n_correct[i] / n_total[i]
            precisions[i] = n_correct[i] / n_pred_total[i]
            fms[i] = (2 * precisions[i] * recalls[i]) / \
                     (precisions[i] + recalls[i])

        return precisions, recalls, fms


def main():
    if len(sys.argv) < 3 or "--help" in sys.argv:
        print(f"Usage: python3 {sys.argv[0]} <train-data> <test-data> "
              "[learn-rate=0.25] [batch-size=10] [epochs=20]")
        exit(1)

    word_vocab, class_vocab = generate_vocabularies(sys.argv[1])
    X_train, y_train = read_labeled_data(sys.argv[1], class_vocab, word_vocab)
    X_test, y_test = read_labeled_data(sys.argv[2], class_vocab, word_vocab)

    num_features = len(word_vocab)
    num_classes = len(class_vocab)

    alpha = 0.25
    if len(sys.argv) > 3:
        alpha = float(sys.argv[3])

    batch_size = 10
    if len(sys.argv) > 4:
        batch_size = int(sys.argv[4])

    epochs = 20
    if len(sys.argv) > 5:
        epochs = int(sys.argv[5])

    lr = LogisticRegression(num_classes, num_features)

    lr.train(X_train, y_train, epochs, alpha, batch_size, verbose=True)

    # Create a reversed class vocabulary that maps class ids to class names.
    reversed_class_vocab = {v: k for k, v in class_vocab.items()}

    # Predict the classes for the test data and compute the precision, recall
    # and f-measure per class.
    precisions, recalls, fms = lr.evaluate(X_test, y_test)

    for i in range(num_classes):
        print(f"\nStats for class \"{reversed_class_vocab[i]}\": ")
        print(f"  Precision:  {precisions[i] * 100:.2f}%")
        print(f"  Recall:     {recalls[i] * 100:.2f}%")
        print(f"  F-score:    {fms[i] * 100:.2f}%")

    # Compute and output the average values.
    avg_precision = sum(precisions.values()) / len(precisions) * 100
    avg_recall = sum(recalls.values()) / len(recalls) * 100
    avg_fmeasure = sum(fms.values()) / len(fms) * 100
    print(f"\nAverage Precision: {avg_precision:.2f}%")
    print(f"Average Recall:    {avg_recall:.2f}%")
    print(f"Average F-score:   {avg_fmeasure:.2f}%\n")


if __name__ == '__main__':
    main()
