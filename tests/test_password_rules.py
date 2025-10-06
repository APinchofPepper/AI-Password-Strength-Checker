from src.password_rules import score_password

def test_short_password():
    assert score_password("abc") < 20

def test_medium_password():
    assert 20 <= score_password("abcABC123") <= 80

def test_strong_password():
    assert score_password("P@ssw0rd123!") >= 80
