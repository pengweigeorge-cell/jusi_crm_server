import uuid
import json
import time
from typing import Dict, Any
from config import settings


def current_timestamp() -> int:
    """获取当前时间戳"""
    return int(time.time())
