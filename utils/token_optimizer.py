def trim_context(texts, max_tokens=2000):

    trimmed = []
    total = 0

    for t in texts:
        length = len(t.split())

        if total + length > max_tokens:
            break

        trimmed.append(t)
        total += length

    return trimmed
