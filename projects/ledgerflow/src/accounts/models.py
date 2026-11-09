from dataclasses import dataclass
from datetime import datetime

@dataclass
class Account:
    id: str
    name: str
    active: bool
    currency: str
    created_at : datetime