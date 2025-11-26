#!/usr/bin/env python3
import json
import pathlib
import re
import sys

URLS_PATH = pathlib.Path("urls.json")

BANNED_SUBSTRINGS = [
    # Adult
    "porn", "xxx", "sex", "xvideos", "xnxx", "redtube", "pornhub",
    "onlyfans", "camgirl", "cam4",
    # Gambling
    "casino", "bet365", "betfair", "poker", "slots", "bookmaker", "1xbet",
    # Basic spammy stuff (tweak as you like)
    "free-money", "giveaway", "crypto-scam",
]

MAX_CODE_LENGTH = 64

def main() -> int:
    try:
        raw = URLS_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("❌ urls.json not found in repo root.")
        return 1

    try:
        data = json.loads(raw)
    except Exception as e:
        print("❌ urls.json is not valid JSON:")
        print("   ", e)
        return 1

    if not isinstance(data, dict):
        print("❌ urls.json must contain a JSON object (key → URL).")
        return 1

    errors: list[str] = []

    for code, url in data.items():
        # ---- validate code ----
        if not isinstance(code, str):
            errors.append(f"Key {code!r} is not a string.")
            continue

        if code != code.lower():
            errors.append(f"Code {code!r} must be lowercase only.")

        if not re.fullmatch(r"[0-9a-z]+", code):
            errors.append(
                f"Code {code!r} must contain only 0–9 and a–z with no spaces."
            )

        if len(code) == 0:
            errors.append("Found an empty code (zero-length key).")

        if len(code) > MAX_CODE_LENGTH:
            errors.append(
                f"Code {code!r} is too long (>{MAX_CODE_LENGTH} characters)."
            )

        # ---- validate URL ----
        if not isinstance(url, str):
            errors.append(f"Value for code {code!r} is not a string.")
            continue

        if not (url.startswith("http://") or url.startswith("https://")):
            errors.append(
                f"URL for code {code!r} must start with http:// or https:// "
                f"(got {url!r})."
            )

        lower_url = url.lower()
        for banned in BANNED_SUBSTRINGS:
            if banned in lower_url:
                errors.append(
                    f"URL for code {code!r} appears disallowed because it "
                    f"contains '{banned}'."
                )
                break

    if errors:
        print("❌ urls.json failed validation. Problems found:")
        for e in errors:
            print("  -", e)
        print("\nPlease fix these before merging this pull request.")
        return 1

    print("✅ urls.json passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
