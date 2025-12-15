# Password Analyzer with GUI

This project analyzes password strength using multiple security techniques.

## Features
- Minimum length, uppercase, lowercase, digit, special character checks
- Shannon entropy calculation
- Dictionary-based weak password detection
- Blacklist and simple pattern detection
- Rate limiting with temporary lockout
- Password hashing using bcrypt
- Tkinter-based GUI


## Türkçe Açıklama

Bu proje, şifre güvenliğini analiz etmek için geliştirilmiş bir Python uygulamasıdır.

### Özellikler
- Minimum uzunluk, büyük/küçük harf, rakam ve özel karakter kontrolleri
- Shannon entropy hesaplaması
- Yaygın şifreler için dictionary kontrolü
- Blacklist ve basit pattern (ör. ardışık rakamlar) tespiti
- Rate limiting (belirli sayıda denemeden sonra geçici kilitleme)
- bcrypt kullanılarak şifre hashleme
- Tkinter tabanlı grafik arayüz (GUI)


## How to Run
```bash
pip install bcrypt
python gui.py



