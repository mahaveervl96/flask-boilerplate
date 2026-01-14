import uuid
import random
import string
from datetime import datetime, timezone

def generate_uuid() -> str:
    return str(uuid.uuid4())

def generate_random_string(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    return dt.strftime(fmt)

def normalize_string(value: str) -> str:
    return value.strip().lower() if value else ""