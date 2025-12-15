import math
import time
import bcrypt

# =========================
# TEMEL KONTROLLER 
# =========================

def has_min_length(pw, min_length=12):
    return len(pw) >= min_length

def has_upper(pw):
    return any(c.isupper() for c in pw)

def has_lower(pw):
    return any(c.islower() for c in pw)

def has_digit(pw):
    return any(c.isdigit() for c in pw)

def has_special(pw):
    special_chars = "!@#$%^&*()-_+=<>?/.,:;[]{}|~`"
    return any(c in special_chars for c in pw)

def calculate_entropy(pw):
    freq = {}
    for c in pw:
        freq[c] = freq.get(c, 0) + 1

    entropy = 0
    length = len(pw)
    for f in freq.values():
        p = f / length
        entropy -= p * math.log2(p)
    return entropy

# =========================
# 1) DICTIONARY CHECK
# =========================

def dictionary_check(pw, filename="common_passwords.txt"):
    try:
        with open(filename, "r") as f:
            common = {line.strip().lower() for line in f}
        return pw.lower() in common
    except FileNotFoundError:
        return False

# =========================
# 2) BLACKLIST + PATTERN
# =========================

def blacklist_check(pw, username=None, birth_year=None):
    blacklist = ["123456", "qwerty", "password", "admin", "iloveyou", "student", "cisco", "azerty", "test123","changeme" ]
    pw_lower = pw.lower()

    if any(word in pw_lower for word in blacklist):
        return True

    if username and username.lower() in pw_lower:
        return True

    if birth_year and str(birth_year) in pw:
        return True

    return False

# =========================
# 4) HASHLEME
# =========================

def hash_password(pw):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw.encode(), salt).decode()

# =========================
# ANA ANALİZ 
# =========================

def analyze_password(pw, username=None, birth_year=None):

    if dictionary_check(pw):
        return "Çok Zayıf (Dictionary)", None, calculate_entropy(pw)

    if blacklist_check(pw, username, birth_year):
        return "Çok Zayıf (Pattern)", None, calculate_entropy(pw)

    entropy = calculate_entropy(pw)

    results = [
        has_min_length(pw),
        has_upper(pw),
        has_lower(pw),
        has_digit(pw),
        has_special(pw),
        entropy >= 3.5
    ]

    passed = sum(results)

    if passed == len(results):
        return "Güçlü", hash_password(pw), entropy
    elif passed >= len(results) / 2:
        return "Orta", hash_password(pw), entropy
    else:
        return "Zayıf", None, entropy

