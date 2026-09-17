def isValid(s: str) -> bool:
    store = []
    map = {'(': ')', '{': '}', '[': ']'}
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] in map:
            store.append(s[l])
        else:
            if not store or map[store.pop()] != s[l]:
                return False
        l += 1
    return not store
