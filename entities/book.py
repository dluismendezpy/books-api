from datetime import datetime

from dataclasses import dataclass


@dataclass
class Book:
    """Entity representing a book"""

    id: int
    title: str
    author: str
    content: str
    pages: int
    created_at: datetime
    last_updated: datetime
