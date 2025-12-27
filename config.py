LT_USERNAME = "gowthamipg892"
LT_ACCESS_KEY = ("LT_7Che5DwiP43uvozMt88lrAEjMsAv93j4a9QfiQE3XKnPCnO")

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
