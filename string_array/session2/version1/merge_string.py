def merge_alternately(word1, word2):
    result = []
    i = 0

    # Alternate while both have characters left
    while i < len(word1) and i < len(word2):
        result.append(word1[i])
        result.append(word2[i])
        i += 1

    # Append remaining characters (if any)
    result.append(word1[i:])
    result.append(word2[i:])

    return "".join(result)