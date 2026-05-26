# Secure Password Generator & Validator 🔐

A cryptographically secure, terminal-based Password Generator built with Python. This application allows users to generate customizable, highly secure passwords and evaluates their strength based on best practices.

---

## ✨ Features
* **Cryptographically Secure:** Powered by `random.SystemRandom()` to ensure true randomness and maximum security against guessing attacks.
* **Fully Customizable:** Users can specify the exact password length (from 4 to 128 characters) and choose whether to include special symbols.
* **Guaranteed Complexity:** The algorithm ensures that at least one character from each selected character group (uppercase, lowercase, digits, symbols) is included in the generated password.
* **Strength Validator:** Evaluates the generated password's complexity using criteria like character diversity and length.

---

## 📁 Project Structure
```text
secure-password-generator-cli/
│
├── password_Generation.py   # Main application script
└── README.md                # Project documentation

How to Run the Project
Prerequisites
You only need Python 3.x installed on your system.

Steps:
Clone the repository:

Bash
git clone [https://github.com/YOUR_USERNAME/secure-password-generator-cli.git](https://github.com/YOUR_USERNAME/secure-password-generator-cli.git)
cd secure-password-generator-cli
Run the app:

Bash
python password_Generation.py
🛠️ Built With
Python 3 (Standard Libraries: random, string)
