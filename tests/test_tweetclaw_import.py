from io import BytesIO
import json
import unittest

from tweetclaw_import import (
    extract_text,
    load_tweet_texts,
    texts_from_csv,
    texts_from_json,
    texts_from_jsonl,
)


class Upload(BytesIO):
    def __init__(self, name, content):
        super().__init__(content.encode("utf-8"))
        self.name = name

    def getvalue(self):
        self.seek(0)
        return super().getvalue()


class TweetClawImportTest(unittest.TestCase):
    def test_extract_text_reads_common_tweet_fields(self):
        self.assertEqual(extract_text({"text": " Hello "}), "Hello")
        self.assertEqual(extract_text({"tweetText": "Alt field"}), "Alt field")
        self.assertEqual(
            extract_text({"tweet": {"full_text": "Nested field"}}),
            "Nested field",
        )
        self.assertIsNone(extract_text({"id": "missing"}))

    def test_texts_from_json_reads_nested_exports(self):
        payload = {
            "tweets": [
                {"text": "First"},
                {"body": "Second"},
                {"tweet": {"content": "Third"}},
                {"text": ""},
            ]
        }

        self.assertEqual(
            texts_from_json(json.dumps(payload)),
            ["First", "Second", "Third"],
        )

    def test_texts_from_jsonl_and_csv(self):
        self.assertEqual(
            texts_from_jsonl('{"text": "One"}\n{"full_text": "Two"}\n'),
            ["One", "Two"],
        )
        self.assertEqual(
            texts_from_csv("id,content\n1,Three\n2,Four\n"),
            ["Three", "Four"],
        )

    def test_load_tweet_texts_uses_file_extension(self):
        self.assertEqual(
            load_tweet_texts(Upload("tweets.ndjson", '{"text": "One"}\n')),
            ["One"],
        )
        self.assertEqual(
            load_tweet_texts(Upload("tweets.csv", "text\nTwo\n")),
            ["Two"],
        )


if __name__ == "__main__":
    unittest.main()
