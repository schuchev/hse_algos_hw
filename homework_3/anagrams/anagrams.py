def anagrams(strs):    
        d = {}
        for s in strs:
            counter = [0] * 26
            for a in s:
                counter[ord(a) - ord("a")] += 1
            d.setdefault(tuple(counter), []).append(s)
        return list(d.values())
    
