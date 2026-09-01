# Python Offline RSA Licensing System (CustomTkinter + PyInstaller)

A complete, production-ready implementation of an **offline RSA-based licensing system** for Python desktop applications. This project demonstrates how to cryptographically verify license keys locally while correctly handling dynamic asset bundles and external configuration files using **PyInstaller**.

---

## 🚀 Features

* **Offline Verification:** No server, API, or active internet connection required. Pure RSA cryptographic validation.
* **Public/Private Key Architecture:** Uses RSA key pairs—embed the public key in your app, sign licenses securely offline with your private key.
* **PyInstaller Ready:** Built-in dynamic path management handling internal bundled assets (`sys._MEIPASS`) vs. external execution directory files.
* **Modern GUI:** Built with `CustomTkinter` for a sleek, contemporary UI.

---

## 🛠 Project Structure

```text
├── app.py              # Main application GUI & RSA verification logic
├── public_key.pem      # RSA Public Key (Bundled INSIDE the executable)
├── license.key         # Signed license file (Placed OUTSIDE next to the .exe)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
💻 Installation & Setup
1. Prerequisites
Ensure you have Python installed, then clone this repository and install the dependencies:

Bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
pip install -r requirements.txt
2. Required Libraries
customtkinter

cryptography

pyinstaller

🔒 How It Works
Path Management: The app utilizes helper functions to distinguish between temporary bundled assets and the execution directory:

Internal Assets (public_key.pem): Accesses resources inside PyInstaller's temporary _MEIPASS folder.

External Assets (license.key): Reads the license key from the directory where the .exe is located.

License Validation: The application loads the embedded public key and attempts to verify the digital signature of license.key. If valid, premium features are unlocked.

📦 Bundling with PyInstaller
To compile the application into a standalone executable while correctly bundling the internal public key, run:

Bash
pyinstaller --noconfirm --onedir --windowed --add-data "public_key.pem;." app.py
Note: Make sure to place a valid license.key file in the output folder next to app.exe before launching the application.

🎥 Video Tutorial
Watch the step-by-step tutorial on YouTube: https://youtu.be/6_3CW9PiQ8U

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
