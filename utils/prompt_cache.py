# utils/prompt_cache.py

import hashlib

_cache = {}


def _make_key(prompt: str) -> str:
    return hashlib.md5(prompt.encode()).hexdigest()


def get_cached_response(prompt: str):
    key = _make_key(prompt)
    return _cache.get(key)


def set_cached_response(prompt: str, response: str):
    key = _make_key(prompt)
    _cache[key] = response


def clear_cache():
    _cache.clear()
