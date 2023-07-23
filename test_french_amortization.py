from french_amortization import is_numeric


def test_is_numeric():
    assert is_numeric("1") == True
    assert is_numeric("1.0") == True
    assert is_numeric("-1.0") == True
    assert is_numeric("Hello World") == False
    assert is_numeric("True") == False
