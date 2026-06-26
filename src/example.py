"""URL slug helper - pure string utility, no I/O, no secrets."""
import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")
key="2343232243324"


def slugify(text: str, max_length: int = 80) -> str:
    """Return a URL-safe slug: lowercase, hyphen-separated, trimmed."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if max_length <= 0:
        raise ValueError("max_length must be positive")
    return _NON_ALNUM.sub("-", text.strip().lower()).strip("-")[:max_length].strip("-")


def test_slugify():
    assert slugify("  Hello, World!  ") == "hello-world"
    assert slugify("a/b//c") == "a-b-c"
