def isValid(s: str) -> bool:
    stack = []
    matches = {"(": ")", "{": "}", "[": "]"}
    for i in s:
        if i in matches:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if matches[stack.pop()] != i:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    assert isValid("()")
    assert isValid("()[]{}")
    assert not isValid("(]")
