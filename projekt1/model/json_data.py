from dataclasses import dataclass
from typing import Any


@dataclass
class JsonData:
    data: dict[str, list[dict[str, Any]]]
