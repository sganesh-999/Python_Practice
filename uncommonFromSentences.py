sentence1 = "the quick brown fox jumps over the lazy dog"
sentence2 = "the quick brown dog jumps over the lazy fox"

def uncommonFromSentences(s1, s2):
    words1 = s1.split()
    words2 = s2.split()

    counts = {}
    for word in words1 + words2:
        counts[word] = counts.get(word, 0) + 1

    uncommon = [word for word in counts if counts[word] == 1]
    return uncommon
print(uncommonFromSentences(sentence1, sentence2))
