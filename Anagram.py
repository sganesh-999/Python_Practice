words = ["tea", "eat", "bat", "ate", "arc", "car"]

def anagram(l):
    d=dict()
    for i in l:
        sorted_l="".join(sorted(i))
        if sorted_l not in d:
            d[sorted_l]=[i]
        else:
            d[sorted_l].append(i)
    print(d.values())
        
    
anagram(words)
