import tkinter as tk
from password_logic import analyze_password

def analyze():
    pw = entry.get()
    strength = analyze_password(pw)
    result_label.config(text=f"Password Strength: {strength}")

# Pencereyi oluştur
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("300x150")

# Label ve input
tk.Label(root, text="Şifrenizi Girin:").pack(pady=5)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

# Analyze button
tk.Button(root, text="Analiz Et", command=analyze).pack(pady=5)

# Sonuç label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
