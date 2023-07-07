def numDistinct(s: str, t: str) -> int:
    cache = {}  # Dictionary to store computed results

    def countDistinctSubsequences(s_index, t_index):
        """
        Recursive function to count the number of distinct subsequences.

        Parameters:
            s_index (int): Index of the current character in string s.
            t_index (int): Index of the current character in string t.

        Returns:
            int: Number of distinct subsequences.
        """
        # Base cases:
        # If we have reached the end of string t, we have found a distinct subsequence
        if t_index == len(t):
            return 1
        # If we have reached the end of string s, there are no more distinct subsequences to find
        if s_index == len(s):
            return 0
        # If the result for the current (s_index, t_index) combination is already computed, return it
        if (s_index, t_index) in cache:
            return cache[(s_index, t_index)]

        # If the characters at the current indices match, we have two possibilities:
        # 1. Include the current character in the subsequence and move to the next characters in both strings
        # 2. Exclude the current character and only move to the next character in string s
        if s[s_index] == t[t_index]:
            # Recursively compute the count of distinct subsequences
            cache[(s_index, t_index)] = countDistinctSubsequences(s_index + 1, t_index + 1) + countDistinctSubsequences(s_index + 1, t_index)
        else:
            # If the characters don't match, exclude the current character and move to the next character in string s
            cache[(s_index, t_index)] = countDistinctSubsequences(s_index + 1, t_index)

        return cache[(s_index, t_index)]

    return countDistinctSubsequences(0, 0)  # Start the recursion from the beginning of both strings


# Example usage
s = "rabbbit"
t = "rabbit"
print("Number of distinct subsequences:", numDistinct(s, t))
