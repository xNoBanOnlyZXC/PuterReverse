<div align="center">
    <h1>PuterReverse</h1>
    Reverse-API of Puter AI API
    <p>Made by <bold>~$ sudo++</bold></p>
    <img alt="code size" src="https://img.shields.io/github/languages/code-size/xnobanonlyzxc/PuterReverse?style=for-the-badge">
    <img alt="repo stars" src="https://img.shields.io/github/stars/xnobanonlyzxc/PuterReverse?style=for-the-badge">
    <img alt="repo stars" src="https://img.shields.io/github/commit-activity/w/xnobanonlyzxc/PuterReverse?style=for-the-badge">
</div>

---
## 🔗 Original Source
- **Original JavaScript SDK**: [https://js.puter.com/v2/](https://js.puter.com/v2/)

---
## 💸 Support Me

If you find this useful, consider donating:

👉 [Donate via DonationAlerts](https://www.donationalerts.com/r/iamsudo)

---
## ⚙️ Configuration

All necessary settings are placed at the top of the file for easy access and configuration.

### 🧠 Token (Required)
```python
token = "eyJhbGciOiJIUzI1..."
```

To obtain a token:
1. Register at [https://puter.com/](https://puter.com/)
2. Open Developer Tools (F12), go to the "Network" tab
3. Copy the `Authorization` header value from any request, taking the string after `Bearer `

---
### 🤖 Available Models

Set your desired model like so:
```python
model = "deepseek-chat"
```

#### ✅ Supported Models:
- `deepseek-chat`
- `deepseek-reasoner`
- `grok-beta`
- `gpt-4.1-nano`
- `gpt-4o-mini`
- `o1`
- `o1-mini`
- `o1-pro`
- `o4-mini`
- `gpt-4.1`
- `gpt-4.1-mini`
- `gpt-4.1-nano`
- `gpt-4.5-preview`
- `claude-sonnet-4-20250514`
- `claude-opus-4-20250514`
- `claude-3-7-sonnet-latest`
- `claude-3-5-sonnet-latest`
- `mistral-large-latest`
- `codestral-latest`

---

### 💬 Message Format

Messages must be formatted as a list of objects with roles and content:
```python
messages = [
    {"role": "user", "content": "Who are you and which model are you using?"}
]
```

#### 📌 Roles:
- `user`
- `system`
- `assistant`

---

### 🔁 Streaming Response Option

Use streaming responses for real-time interaction:
```python
stream = True
```

Set to `False` if you prefer receiving the full response at once.
