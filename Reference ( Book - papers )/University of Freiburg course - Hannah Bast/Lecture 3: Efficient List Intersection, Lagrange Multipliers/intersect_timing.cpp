// Copyright 2022, University of Freiburg
// Chair of Algorithms and Data Structures
// Author: Hannah Bast <bast@cs.uni-freiburg.de>,

#include <algorithm>
#include <chrono>
#include <iostream>
#include <limits>
#include <random>
#include <vector>

// Intersecting two lists of sorted integers using the basic linear-time
// "zipper" algorithm.
std::vector<int> intersect_1(const std::vector<int>& A,
                             const std::vector<int>& B) {
  std::vector<int> result;
  size_t i = 0;
  size_t j = 0;
  while (i < A.size() && j < B.size()) {
    if (A[i] < B[j]) { i += 1; }
    if (i == A.size()) { break; }
    if (B[j] < A[i]) { j += 1; }
    if (j == B.size()) { break; }
    if (A[i] == B[j]) {
      result.push_back(A[i]);
      i += 1;
      j += 1;
    }
  }
  return result;
}

// Variant 2: fewer ifs.
std::vector<int> intersect_2(const std::vector<int>& A,
                             const std::vector<int>& B) {
  std::vector<int> result;
  size_t i = 0;
  size_t j = 0;
  while (i < A.size() && j < B.size()) {
    if (A[i] < B[j]) {
      i += 1;
    } else if (B[j] < A[i]) {
      j += 1;
    } else {
      result.push_back(A[i]);
      i += 1;
      j += 1;
    }
  }
  return result;
}

// Variant 3: skip over longer segments using a while loop.
std::vector<int> intersect_3(const std::vector<int>& A,
                             const std::vector<int>& B) {
  std::vector<int> result;
  size_t i = 0;
  size_t j = 0;
  while (i < A.size() && j < B.size()) {
    while (i < A.size() && A[i] < B[j]) { i += 1; }
    if (i == A.size()) { break; }
    while (j < B.size() && B[j] < A[i]) { j += 1; }
    if (j == B.size()) { break; }
    if (A[i] == B[j]) {
      result.push_back(A[i]);
      i += 1;
      j += 1;
    }
  }
  return result;
}

// Variant 4: Use constants for A.size() and B.size().
std::vector<int> intersect_4(const std::vector<int>& A,
                             const std::vector<int>& B) {
  std::vector<int> result;
  size_t i = 0;
  size_t j = 0;
  const size_t n1 = A.size();
  const size_t n2 = B.size();
  while (i < n1 && j < n2) {
    while (i < n1 && A[i] < B[j]) { i += 1; }
    if (i == n1) { break; }
    while (j < n2 && B[j] < A[i]) { j += 1; }
    if (j == n2) { break; }
    if (A[i] == B[j]) {
      result.push_back(A[i]);
      i += 1;
      j += 1;
    }
  }
  return result;
}

// Variant 5: Use sentinels.
std::vector<int> intersect_5(std::vector<int>& A,
                             std::vector<int>& B) {
  std::vector<int> result;
  size_t i = 0;
  size_t j = 0;
  const size_t n1 = A.size();
  const size_t n2 = B.size();
  // A.push_back(std::numeric_limits<int>::infinity());
  // B.push_back(std::numeric_limits<int>::infinity());
  A.back() = std::numeric_limits<int>::infinity();
  B.back() = std::numeric_limits<int>::infinity();
  while (i < n1 && j < n2) {
    while (A[i] < B[j]) { i += 1; }
    if (i == n1) { break; }
    while (B[j] < A[i]) { j += 1; }
    if (j == n2) { break; }
    if (A[i] == B[j]) {
      result.push_back(A[i]);
      i += 1;
      j += 1;
    }
  }
  // A.pop_back();
  // B.pop_back();
  return result;
}

// _____________________________________________________________________________
int main(int argc, char **argv) {
  // Parse command line arguments.
  if (argc != 4) {
    std::cerr << "Usage: ./intersect_timing <n1> <n2> <k>" << std::endl;
    exit(1);
  }
  size_t n1 = atol(argv[1]);
  size_t n2 = atol(argv[2]);
  int k = atoi(argv[3]);

  // Create random sorted lists of lengths n1 and n2, respectively.
  std::mt19937 random_source;
  std::uniform_int_distribution<std::mt19937::result_type> random_int(0, n1 + n2);
  std::vector<int> A(n1);
  std::vector<int> B(n2);
  std::generate(A.begin(), A.end(),
                [&]() { return random_int(random_source); });
  std::generate(B.begin(), B.end(),
                [&]() { return random_int(random_source); });
  std::sort(A.begin(), A.end());
  std::sort(B.begin(), B.end());
  // A.reserve(n1 + 1);
  // B.reserve(n2 + 1);

  // Intersect the two lists and measure the time (do it three times).
  for (int run = 1; run <= 3; ++run) {
    std::cout << "Intersecting two lists of sizes "
              << n1 << " and " << n2 << " ... " << std::flush;
    auto time1 = std::chrono::high_resolution_clock::now();
    std::vector<int> result;
    switch (k) {
      case 1: result = intersect_1(A, B); break;
      case 2: result = intersect_2(A, B); break;
      case 3: result = intersect_3(A, B); break;
      case 4: result = intersect_4(A, B); break;
      case 5: result = intersect_5(A, B); break;
      default:
        std::cerr << "ERROR: intersect_" << k << " not defined" << std::endl;
	exit(1);
    }
    auto time2 = std::chrono::high_resolution_clock::now();
    size_t time = std::chrono::duration_cast<std::chrono::milliseconds>
                    (time2 - time1).count();
    std::cout << time << " ms, result size = " << result.size()
              << std::endl;
  }
}
