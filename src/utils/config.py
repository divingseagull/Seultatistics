import tomllib
from typing import Any


def get_config() -> dict[str, Any]:
    with open("config.toml", "rb") as f:
        return tomllib.load(f)
