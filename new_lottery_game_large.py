def getBit(num, i):
  return (num >> i) & 1  # Returns the i-th bit value of num.
def countPairs(i, lessA, lessB, lessK, A, B, K):
  if i == -1:  # The base case.
    return lessA and lessB and lessK  # Count those that are strictly less.

  maxA = lessA or getBit(A, i) == 1
  maxB = lessB or getBit(B, i) == 1
  maxK = lessK or getBit(K, i) == 1

  # Use value 0 for a, b, and k which is always possible. See (1).
  count = countPairs(i - 1, maxA, maxB, maxK, A, B, K)

  if maxA:  # Use value 1 for a, and 0 for b and k. See (2).
    count += countPairs(i - 1, lessA, maxB, maxK, A, B, K)

  if maxB:  # Use value 1 for b, and 0 for a and k. See (3)
    count += countPairs(i - 1, maxA, lessB, maxK, A, B, K)

  if maxA and maxB and maxK:  # Use value 1 for a, b, and k. See (4)
    count += countPairs(i - 1, lessA, lessB, lessK, A, B, K)

  return count
print countPairs(31,0,0,0,103,143,88)