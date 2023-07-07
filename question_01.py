import sys


def matrixChainMultiplication(dims, i, j):
    """
    Recursive function to compute the minimum cost of matrix chain multiplication.

    Parameters:
        dims (list): List of matrix dimensions.
        i (int): Starting index of the current subproblem.
        j (int): Ending index of the current subproblem.

    Returns:
        int: Minimum cost of matrix chain multiplication for the given subproblem.
    """
    # Base case: Only one matrix, return 0 cost
    if j <= i + 1:
        return 0

    min_cost = sys.maxsize  # Initialize minimum cost to a large value

    # Iterate through possible splitting points
    for k in range(i + 1, j):
        # Compute the cost for the current splitting point
        cost = (
            # Cost of multiplying matrices from i to k
            matrixChainMultiplication(dims, i, k) +
            # Cost of multiplying matrices from k+1 to j
            matrixChainMultiplication(dims, k, j) +
            # Cost of multiplying the resulting matrices
            dims[i] * dims[k] * dims[j]
        )
        if cost < min_cost:
            min_cost = cost

    return min_cost


if __name__ == '__main__':
    # Matrix dimensions, use square brackets for the list
    dims = [10, 30, 5, 60]

    print('The minimum cost is', matrixChainMultiplication(dims, 0, len(dims) - 1))
