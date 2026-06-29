import csv
import json
from io import StringIO

TEXT_COLUMNS = ("text", "full_text", "tweetText", "content", "body")
COLLECTION_KEYS = ("tweets", "items", "data", "results")


def extract_text(record):
    if isinstance(record, str):
        value = record.strip()
        return value or None

    if not isinstance(record, dict):
        return None

    for key in TEXT_COLUMNS:
        value = record.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()

    tweet = record.get("tweet")
    if isinstance(tweet, dict):
        return extract_text(tweet)

    return None


def records_from_json(payload):
    if isinstance(payload, list):
        return payload

    if isinstance(payload, dict):
        for key in COLLECTION_KEYS:
            value = payload.get(key)
            if isinstance(value, list):
                return value
        return [payload]

    return []


def texts_from_json(content):
    payload = json.loads(content)
    return [text for record in records_from_json(payload) if (text := extract_text(record))]


def texts_from_jsonl(content):
    texts = []
    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue

        text = extract_text(json.loads(line))
        if text:
            texts.append(text)

    return texts


def texts_from_csv(content):
    rows = list(csv.DictReader(StringIO(content)))
    for column in TEXT_COLUMNS:
        if rows and column in rows[0]:
            return [
                str(row[column]).strip()
                for row in rows
                if row.get(column) and str(row[column]).strip()
            ]

    return []


def load_tweet_texts(uploaded_file):
    name = uploaded_file.name.lower()
    content = uploaded_file.getvalue().decode("utf-8")

    if name.endswith(".jsonl") or name.endswith(".ndjson"):
        return texts_from_jsonl(content)

    if name.endswith(".csv"):
        return texts_from_csv(content)

    return texts_from_json(content)
