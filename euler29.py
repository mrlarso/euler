def count_distinct(limit):
    terms = []
    for a in range(2,limit+1):
        for b in range(2,limit+1):
            if a**b not in terms:
                terms.append(a**b)
    return len(terms)

print count_distinct(100)
