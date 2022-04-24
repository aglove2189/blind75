def isValid(s: str) -> bool:
    pass


if __name__ == "__main__":
    assert isValid("()")
    assert isValid("()[]{}")
    assert not isValid("(]")
