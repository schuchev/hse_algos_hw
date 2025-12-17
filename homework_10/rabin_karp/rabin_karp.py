def rabin_karp(text, pattern):

    N, M = len(text), len(pattern)
    if M == 0:
        return 0
    if M > N:
        return -1

    p = 31        
    mod = 10**9+7  

    pattern_hash = 0
    for c in pattern:
        pattern_hash = (pattern_hash * p + ord(c)) % mod

    text_hash = 0
    p_pow = 1  
    for i in range(M):
        text_hash = (text_hash * p + ord(text[i])) % mod
        if i < M-1:
            p_pow = (p_pow * p) % mod

    for i in range(N - M + 1):
        if text_hash == pattern_hash:
            if text[i:i+M] == pattern:
                return i
        if i < N - M:
            text_hash = (text_hash - ord(text[i]) * p_pow) % mod
            text_hash = (text_hash * p + ord(text[i + M])) % mod
            text_hash = (text_hash + mod) % mod 

    return -1
