# Reversed puter.js API by iamsudo (NoBanOnlyZXC)
# Used in OnlySq API since 30.06.2025
# Original (javascript): https://js.puter.com/v2/
# Donate: https://www.donationalerts.com/r/iamsudo

# Все нужные настройки выведены в верх файла.

# Эта строка является токеном. Без него не будет работать.
token = ""
# Для получения токена нужно:
# 1. Перейти на https://puter.com/ и пройти регистрацию
# 2. В панели разработчика, в разделе "сеть" в заголовках любого запроса скопировать строку Authorization после "Bearer "

# Обращаться к модели:
model = "deepseek-chat"
# Список моделей:
# deepseek-chat
# deepseek-reasoner
# grok-beta
# gpt-4.1-nano
# gpt-4o-mini
# o1
# o1-mini
# o1-pro
# o4-mini
# gpt-4.1
# gpt-4.1-mini
# gpt-4.1-nano
# gpt-4.5-preview
# claude-sonnet-4-20250514
# claude-opus-4-20250514
# claude-3-7-sonnet-latest
# claude-3-5-sonnet-latest
# mistral-large-latest
# codestral-latest

# Формат сообщений:
# {"role":"role","content": "text"}
# Роли: user, system, assistant
messages = [
    {"role":"user","content": "Кто ты и какая модель?"}
]

# Использовать поточный вариант ответов
stream = True 

# -- BEGIN CODE --
import requests, json

url = "https://api.puter.com/drivers/call"
headers = {
    "Host": "api.puter.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json;charset=UTF-8",
    "Content-Length": "154",
    "Origin": "https://docs.puter.com ",
    "Connection": "keep-alive",
    "Referer": "https://docs.puter.com/ ",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "DNT": "1",
    "Sec-GPC": "1",
    "Idempotency-Key": "\"4900243693008804770\"",
    "TE": "trailers"
}

class d:
    deepseek = [
        "deepseek-chat",
        "deepseek-reasoner"
    ]

    xai = [
        "grok-beta"
    ]

    openai = [
        "gpt-4.1-nano",
        "gpt-4o-mini",
        "o1",
        "o1-mini",
        "o1-pro",
        "o4-mini",
        "gpt-4.1",
        "gpt-4.1-mini",
        "gpt-4.1-nano",
        "gpt-4.5-preview"
    ]

    claude = [
        "claude-sonnet-4-20250514",
        "claude-opus-4-20250514",
        "claude-3-7-sonnet-latest",
        "claude-3-5-sonnet-latest",
    ]

    mistral = [
        "mistral-large-latest",
        "codestral-latest"
    ]

match model:
    case m if m in d.deepseek:
        driver = "deepseek"
    case m if m in d.xai:
        driver = "xai"
    case m if m in d.claude:
        driver = "claude"
    case m if m in d.mistral:
        driver = "mistral"
    case m if m in d.openai:
        driver = "openai-completion"

data = {
    "interface": "puter-chat-completion",
    "driver": driver,
    "test_mode": False,
    "method": "complete",
    "args": {
        "messages": messages,
        "model": model,
        "stream": stream
    }
}

response = requests.post(url, headers=headers, json=data, stream=stream)

print(f"Code {response.status_code}")
if response.status_code == 200:
    if stream:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                usage = [0,0,0]
                try:
                    chunk = json.loads(decoded_line)
                    part = chunk.get("text", "")
                                
                    print(part, end="")
                except json.JSONDecodeError:
                    continue
        print()
        print("data: [DONE]\n\n")
    else:
        text = response.json().get("result", {}).get("message", {}).get("content", "No text, maybe error?")
        if driver == "claude":
            text = text[0]["text"]
        _ = response.json().get("result", {}).get("usage", [])
        usage = [
            x["amount"] for x in _
        ] if _.__class__ != dict else [
            _["input_tokens"], _["output_tokens"]
        ]
        usage.append(sum(usage))
        print(text)
        print(usage)
# -- END CODE --