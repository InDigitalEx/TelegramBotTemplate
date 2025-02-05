from abc import ABC
from dataclasses import dataclass
from typing import Final


@dataclass
class Messages(ABC):
    START: Final = 'Hello, your telegram id is <b>{telegram_id}</b>'
