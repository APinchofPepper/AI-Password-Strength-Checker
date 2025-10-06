import re

def score_password(password: str) -> int:
    """
    Scores a password based on length, character variety, and complexity.
    Returns an integer from 0–100.
    """
    score = 0

    # Length points
    if len(password) >= 8:
        score += 20
    if len(password) >= 12:
        score += 10

    # Character variety
    if re.search(r"[a-z]", password):
        score += 10
    if re.search(r"[A-Z]", password):
        score += 10
    if re.search(r"\d", password):
        score += 10
    if re.search(r"[^A-Za-z0-9]", password):
        score += 10

    # Bonus for diversity
    unique_chars = len(set(password))
    if unique_chars > 6:
        score += min(20, unique_chars)  # cap bonus

    # Cap at 100
    return min(score, 100)


if __name__ == "__main__":
    test_pw = "P@ssw0rd123"
    print(f"Password: {test_pw} | Score: {score_password(test_pw)}")
