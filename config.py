LT_USERNAME = "gowthamipg8888"
LT_ACCESS_KEY = "KFIGD3VUgMMQlkEMKqdowcIOwd0zlwMwrIHaMfNRH0CNVfN3vZ"

LT_OPTIONS = {
    "user": LT_USERNAME,
    "accessKey": LT_ACCESS_KEY,
    "build": "Playwright Parallel Demo",
    "platform": "Windows 10",
    "video": True,
    "network": True,
    "console": True
}

# Duplicate Chrome ONLY for parallel execution
BROWSERS = [
    {"browserName": "pw-chromium"},
    {"browserName": "pw-chromium"}
]
