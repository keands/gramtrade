buy_pattern = r"\b(buy|long|achat)\b"
short_pattern = r"\b(sell|short|vente)\b"

buy_limit_pattern = r"\b(buy limit)\b"
sell_limit_pattern = r"\b(sell limit)\b"

entry_pattern = r"\b(entrée|entry|pe|actuel|@)\b"

regex_decimal = r"\s?\d+[.,]?\d+\s?"

major_pairs = [
    "XAUUSD",
    "EURUSD",
    "USDJPY",
    "GBPUSD",
    "AUDUSD",
    "USDCHF"
]

minor_pairs = [
    "EURGBP",
    "EURCHF",
    "EURJPY",
    "GBPJPY",
    "AUDJPY",
    "GBPAUD",
    "EURAUD"
]
