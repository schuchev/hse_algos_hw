def lcs(string_1, string_2):
    n = len(string_1)
    m = len(string_2)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string_1[i - 1] == string_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    lcs_str = []
    while i > 0 and j > 0:
        if string_1[i - 1] == string_2[j - 1]:
            lcs_str.append(string_1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_str))
