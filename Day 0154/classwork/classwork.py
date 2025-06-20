def word_search(query, seq):
    result = [s for s in seq if query.lower() in s.lower()]
    return result if result else ["None"]