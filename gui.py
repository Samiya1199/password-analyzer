import tkinter as tk
from password_analyzer import analyze_password

MAX_TRIES = 5
LOCK_TIME = 30

tries_left = MAX_TRIES
lock_seconds = LOCK_TIME
locked = False
current_hash = None

def analyze():
    global tries_left, locked, current_hash

    if locked:
        return

    pw = entry.get()
    strength, hashed, entropy = analyze_password(pw)

    # ---- Risk rengi ----
    if "Güçlü" in strength:
        color = "green"
    elif "Orta" in strength:
        color = "orange"
    else:
        color = "red"

    result_label.config(text=f"Password Strength: {strength}", fg=color)
    entropy_label.config(text=f"Entropy: {entropy:.2f}")

    if strength.startswith("Çok Zayıf") or strength == "Zayıf":
        tries_left -= 1
        counter_label.config(text=f"Kalan deneme: {tries_left}/{MAX_TRIES}")

    if hashed:
        current_hash = hashed
        hash_label.config(text=f"Hash:\n{hashed}")
        copy_button.config(state="normal")
    else:
        current_hash = None
        hash_label.config(text="")
        copy_button.config(state="disabled")

    if tries_left == 0:
        lock_system()

def copy_hash():
    if current_hash:
        root.clipboard_clear()
        root.clipboard_append(current_hash)

def lock_system():
    global locked
    locked = True
    analyze_button.config(state="disabled")
    countdown()

def countdown():
    global lock_seconds, tries_left, locked

    if lock_seconds > 0:
        countdown_label.config(
            text=f"Sistem kilitli. {lock_seconds} saniye sonra tekrar deneyin."
        )
        lock_seconds -= 1
        root.after(1000, countdown)
    else:
        locked = False
        lock_seconds = LOCK_TIME
        tries_left = MAX_TRIES
        counter_label.config(text=f"Kalan deneme: {tries_left}/{MAX_TRIES}")
        countdown_label.config(text="")
        analyze_button.config(state="normal")

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Advanced Password Analyzer")
root.geometry("470x420")

tk.Label(root, text="Şifrenizi Girin:").pack(pady=5)

entry = tk.Entry(root, show="*", width=32)
entry.pack(pady=5)

analyze_button = tk.Button(root, text="Analiz Et", command=analyze)
analyze_button.pack(pady=10)

counter_label = tk.Label(root, text=f"Kalan deneme: {MAX_TRIES}/{MAX_TRIES}", fg="blue")
counter_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack(pady=5)

entropy_label = tk.Label(root, text="Entropy: -")
entropy_label.pack()

countdown_label = tk.Label(root, text="", fg="red")
countdown_label.pack(pady=5)

hash_label = tk.Label(root, text="", wraplength=430, fg="gray")
hash_label.pack(pady=5)

copy_button = tk.Button(root, text="Hash Kopyala", state="disabled", command=copy_hash)
copy_button.pack(pady=5)

root.mainloop()

