import math

# Minimum uzunluk kontrolü
def has_min_length(pw, min_length=12):
    return len(pw) >= min_length

# Büyük harf kontrolü
def has_upper(pw):
    for c in pw:
        if c.isupper():
            return True
    return False

# Küçük harf kontrolü
def has_lower(pw):
    for c in pw:
        if c.islower():
            return True
    return False

# Rakam kontrolü
def has_digit(pw):
    for c in pw:
        if c.isdigit():
            return True
    return False

# Özel karakter kontrolü
def has_special(pw):
    special_chars = "!@#$%^&*()-_+=<>?/.,:;[]{}|~`"
    for c in pw:
        if c in special_chars:
            return True
    return False

# Entropy hesaplama fonksiyonu

def calculate_entropy(pw):
    # Her karakterin frekansını say
    freq = {}
    for c in pw:
        freq[c] = freq.get(c, 0) + 1

    # Shannon entropy formülü
    entropy = 0
    length = len(pw)
    for f in freq.values():
        p = f / length
        entropy -= p * math.log2(p)
    return entropy

# Ana analiz fonksiyonu
def analyze_password(pw):
    results = {
        "Min Length": has_min_length(pw),
        "Uppercase": has_upper(pw),
        "Lowercase": has_lower(pw),
        "Digit": has_digit(pw),
        "Special Character": has_special(pw),
        "Entropy >= 3.5": calculate_entropy(pw) >= 3.5,
    }


    # Basit Strength değerlendirmesi
    passed = sum(value for value in results.values())
    if passed == len(results):
        strength = "Güçlü"
    elif passed >= len(results) / 2:
        strength = "Orta"
    else:
        strength = "Zayıf"

    return strength
