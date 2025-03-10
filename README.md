# 🚀 PayloadCheckers

PayloadCheckers is a Python3-based tool designed for automated security testing of XSS, XXE, SQLi, and other payloads against web applications. It efficiently identifies vulnerabilities and is fully independent of external dependencies.

---

## **🔧 Features**
✅ Multi-threaded execution using `multiprocessing.Pool` for high-speed testing  
✅ Supports custom payload lists (`-w <wordlist.txt>`)  
✅ Automatically generates logs (`log_payloads/`, `log_err/`)  
✅ ASCII Art banner independent of system dependencies  
✅ Customizable User-Agent (`ua.txt` allows adding multiple user agents)  
✅ Supports testing on specific ports (`-p <port>`)  

---

## **📥 Installation**
This tool is designed to run on **Python3 only** and does not require any additional dependencies.


---

## **🚀 Usage**
### **🔹 Basic Execution**
```bash
python3 payload_checkers.py -url "https://example.com" -w payloads.txt
```

### **🔹 Available Options**
| Option | Description |
|--------|-------------|
| `-url` | Target URL (e.g., `https://example.com`) |
| `-w` | Payload wordlist file (e.g., `xss_payloads.txt`) |
| `-m` | HTTP method (`GET` / `POST`) |
| `-p` | Custom port number (default: `80` / `443`) |
| `-t` | Number of threads (default: `4`) |

---

## **📂 Logging**
✅ `log_payloads/` stores **payload execution logs**  
✅ `log_err/` stores **error logs (`traceback.format_exc()`)**  

---

## **💡 Examples**
### **🔹 GET Request Payload Testing**
```bash
python3 payload_checkers.py -url "https://target.com" -w xss_payloads.txt -m GET
```

### **🔹 POST Request Payload Testing**
```bash
python3 payload_checkers.py -url "https://target.com" -w sqli_payloads.txt -m POST
```

### **🔹 Testing on Custom Port 8080**
```bash
python3 payload_checkers.py -url "https://target.com" -w payloads.txt -p 8080
```

---

## **🎨 ASCII Banner**
PayloadCheckers displays a **cool ASCII banner** upon execution!

```
▗▄▄▖  ▗▄▖▗▖  ▗▖▗▖    ▗▄▖  ▗▄▖ ▗▄▄▄      ▗▄▄▖▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▖  ▗▄▄▖
▐▌ ▐▌▐▌ ▐▌▝▚▞▘ ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌  █    ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌▗▞▘▐▌   ▐▌ ▐▌▐▌
▐▛▀▘ ▐▛▀▜▌ ▐▌  ▐▌   ▐▌ ▐▌▐▛▀▜▌▐▌  █    ▐▌   ▐▛▀▜▌▐▛▀▀▘▐▌   ▐▛▚▖ ▐▛▀▀▘▐▛▀▚▖ ▝▀▚▖
▐▌   ▐▌ ▐▌ ▐▌  ▐▙▄▄▖▝▚▄▞▘▐▌ ▐▌▐▙▄▄▀    ▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌▗▄▄▞▘

```

---

## **⚠️ Disclaimer**
This tool is intended **for security research and testing only**.  
**Unauthorized testing on third-party systems is illegal** and could result in legal consequences.  

> **The developer assumes no liability for the misuse of this tool.**

---

## **📜 License**
This project is licensed under the **MIT License**.  
You are free to use and modify it, but must comply with the license terms when using it for commercial purposes.

---

## **🌍 Contributing**
**Bug reports, feature requests, and pull requests are welcome!** 🚀  
Feel free to open an issue or submit a pull request on GitHub.  

---

## **📩 Contact**
Developer: **[Alecto-Fsociety](https://github.com/Alecto-Fsociety)**  
GitHub: **[https://github.com/Alecto-Fsociety/PayloadCheckers](https://github.com/Alecto-Fsociety/PayloadCheckers)**  
Proton Mail: **[ goodbye_friend1111@proton.me]**
```

