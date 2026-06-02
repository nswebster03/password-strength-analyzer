import re

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty",
    "abc123", "password123", "admin", "letmein"
}

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This password is too common.")

    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid repeated characters like aaa or 111.")

    if re.search(r"1234|abcd|qwerty|password", password.lower()):
        feedback.append("Avoid common patterns like 1234, abcd, or password.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }